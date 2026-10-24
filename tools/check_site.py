"""Check generated page metadata, internal links, assets, and opening hours."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
import json
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]

class Page(HTMLParser):
    def __init__(self, path):
        super().__init__(convert_charrefs=True)
        self.path, self.ids, self.links, self.scripts, self.metas = path, set(), [], [], {}
        self.h1_count = 0
        self.script = None
        self.canonical = None
        self.feed(path.read_text(encoding='utf-8'))

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            assert attrs['id'] not in self.ids, f'{self.path.name}: duplicate id'
            self.ids.add(attrs['id'])
        if tag == 'h1': self.h1_count += 1
        if tag == 'meta': self.metas[attrs.get('name') or attrs.get('property')] = attrs.get('content')
        if tag == 'link' and attrs.get('rel') == 'canonical': self.canonical = attrs.get('href')
        if tag == 'img': assert 'alt' in attrs, f'{self.path.name}: image missing alt text'
        if tag == 'script' and attrs.get('type') == 'application/ld+json': self.script = ''
        for attribute in ('src', 'href'):
            if attribute in attrs: self.links.append(attrs[attribute])

    def handle_data(self, data):
        if self.script is not None: self.script += data

    def handle_endtag(self, tag):
        if tag == 'script' and self.script is not None:
            self.scripts.append(json.loads(self.script))
            self.script = None

pages = {p.name: Page(p) for p in ROOT.glob('*.html')}
descriptions = set()
for name, page in pages.items():
    assert page.h1_count == 1, f'{name}: expected one H1'
    assert page.canonical and page.canonical.startswith('https://naturescures.in/'), f'{name}: invalid canonical'
    description = page.metas.get('description')
    assert description and description not in descriptions, f'{name}: missing or duplicate description'
    descriptions.add(description)
    clinic = page.scripts[0]['@graph'][0]
    assert clinic['telephone'] == '+919412276843'
    assert clinic['name'] == 'Nature’s Cure Wellness & Regimen Therapy Centre'
    hours = clinic['openingHoursSpecification']
    assert [(x['opens'], x['closes']) for x in hours] == [('10:00', '17:00'), ('00:00', '00:00'), ('10:00', '14:00')]
    for link in page.links:
        parsed = urlsplit(link)
        if parsed.scheme or parsed.netloc: continue
        target = unquote(parsed.path)
        target = 'index.html' if target in ('', './') else target
        target_path = ROOT / target
        assert target_path.is_file(), f'{name}: broken file link: {link}'
        if parsed.fragment and target_path.suffix == '.html':
            target_page = page if not parsed.path else pages[target_path.name]
            assert unquote(parsed.fragment) in target_page.ids, f'{name}: broken anchor: {link}'
    print(f'PASS {name}: heading, metadata, structured data, links, images, and hours')

urls = [x.text for x in ET.parse(ROOT / 'sitemap.xml').iter('{http://www.sitemaps.org/schemas/sitemap/0.9}loc')]
assert len(urls) == 4 and not any('404' in x for x in urls)
assert (ROOT / 'CNAME').read_text().strip() == 'naturescures.in'
assert 'https://naturescures.in/sitemap.xml' in (ROOT / 'robots.txt').read_text()
print('PASS sitemap.xml, robots.txt, and CNAME')
