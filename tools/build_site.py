"""Generate the static, dependency-free GitHub Pages website. Run from any folder."""
from pathlib import Path
from html import escape
import json
from urllib.parse import urlencode

ROOT = Path(__file__).resolve().parents[1]
DOMAIN = 'https://naturescures.in'
NAME = 'Dr. Mohammad Muhiul Haque Siddiqui'
ADDRESS = 'Anoop Sheher Road, behind ACN Ayurvedic Hospital, Greenpark, Manjur Garhi, Aligarh, Uttar Pradesh 202001, India'
PHONE = '+91 94122 76843'
EMAIL = 'muhiul.haque@gmail.com'
MAP = 'https://www.google.com/maps/search/?' + urlencode({'api': '1', 'query': ADDRESS})
TEL = 'tel:+919412276843'
HOURS = '<div class="hours"><div><span>Monday–Thursday</span><strong>10:00 am–5:00 pm</strong></div><div><span>Friday</span><strong>Closed</strong></div><div><span>Saturday–Sunday</span><strong>10:00 am–2:00 pm</strong></div><small>All timings are in India Standard Time (IST).</small></div>'
HOURS_SCHEMA = [
    {'@type': 'OpeningHoursSpecification', 'dayOfWeek': ['https://schema.org/Monday', 'https://schema.org/Tuesday', 'https://schema.org/Wednesday', 'https://schema.org/Thursday'], 'opens': '10:00', 'closes': '17:00'},
    {'@type': 'OpeningHoursSpecification', 'dayOfWeek': ['https://schema.org/Friday'], 'opens': '00:00', 'closes': '00:00'},
    {'@type': 'OpeningHoursSpecification', 'dayOfWeek': ['https://schema.org/Saturday', 'https://schema.org/Sunday'], 'opens': '10:00', 'closes': '14:00'},
]

PATHS = {
    'arrow': '<path d="M5 12h14m-6-6 6 6-6 6"/>',
    'phone': '<path d="m7 3 3 5-3 3a17 17 0 0 0 6 6l3-3 5 3-1 4C11 23 1 13 3 4Z"/>',
    'pin': '<path d="M20 10c0 6-8 12-8 12S4 16 4 10a8 8 0 1 1 16 0Z"/><circle cx="12" cy="10" r="2.5"/>',
    'leaf': '<path d="M4 20C0 8 10 2 21 3c1 11-5 21-17 17Zm0 0L16 8m-8 8v-6m0 6h6"/>',
    'book': '<path d="M12 5c-3-2-7-2-10-1v15c4-1 7-1 10 1 3-2 6-2 10-1V4c-3-1-7-1-10 1Zm0 0v15"/>',
    'person': '<circle cx="12" cy="7" r="4"/><path d="M4 22v-3a8 8 0 0 1 16 0v3M9 17l3 3 3-3"/>',
    'heart': '<path d="M12 21S2 15 2 8a5 5 0 0 1 10-2A5 5 0 0 1 22 8c0 7-10 13-10 13Z"/><path d="M6 12h3l2-4 2 8 2-4h3"/>',
    'clock': '<circle cx="12" cy="12" r="9"/><path d="M12 6v6l4 2"/>',
    'mail': '<rect x="2" y="4" width="20" height="16" rx="2"/><path d="m2 6 10 7L22 6"/>',
    'menu': '<path d="M4 6h16M4 12h16M4 18h16"/>',
}

def icon(name):
    return f'<svg class="icon" viewBox="0 0 24 24" aria-hidden="true">{PATHS[name]}</svg>'

def button(label, href=TEL, kind='', glyph='arrow'):
    return f'<a class="button {kind}" href="{escape(href, quote=True)}">{label}{icon(glyph)}</a>'

def text_link(label, href):
    return f'<a class="text-link" href="{href}">{label}{icon("arrow")}</a>'

def brand():
    return '<a class="brand" href="./" aria-label="Nature’s Cure home"><img src="assets/favicon.svg" width="44" height="44" alt=""><span>Nature’s Cure<small>Wellness &amp; Regimen Therapy Centre</small></span></a>'

def portrait():
    return f'''<div class="doctor-panel"><div class="portrait-crop"><img src="images/mmh_siddiqui.png" alt="Portrait of {NAME}" width="1122" height="1402" loading="lazy"></div><div class="portrait-label"><strong>Prof. {NAME}</strong><small>BUMMS · M.D. (Ilmul Advia) · M.D. (Moalejat)</small></div></div>'''

def visit_banner():
    return f'''<section class="section"><div class="container"><div class="visit-banner"><div><span class="eyebrow">Visit us in Aligarh</span><h2>Let’s begin with<br>a conversation.</h2><p>Call to discuss a consultation and confirm clinic timings before you visit.</p><div class="button-row">{button('Call the clinic', kind='light', glyph='phone')}</div></div><div class="visit-details"><div class="detail">{icon('pin')}<div><small>Find the clinic</small><p>{ADDRESS}</p></div></div><div class="detail">{icon('phone')}<div><small>Speak with us</small><a href="{TEL}">{PHONE}</a></div></div><div class="detail">{icon('clock')}<div><small>Plan your visit</small><p>Please call to confirm availability.</p></div></div></div></div></div></section>'''

def page_hero(label, title, lead):
    return f'''<section class="page-hero"><div class="container"><nav class="breadcrumb" aria-label="Breadcrumb"><a href="./">Home</a><span aria-hidden="true">/</span><span>{label}</span></nav><span class="eyebrow">Nature’s Cure · Aligarh</span><h1>{title}</h1><p class="lead">{lead}</p></div></section>'''

def schema(filename, title, description):
    address = {'@type': 'PostalAddress', 'streetAddress': 'Anoop Sheher Road, behind ACN Ayurvedic Hospital, Greenpark, Manjur Garhi', 'addressLocality': 'Aligarh', 'addressRegion': 'Uttar Pradesh', 'postalCode': '202001', 'addressCountry': 'IN'}
    url = DOMAIN + ('/' if filename == 'index.html' else '/' + filename)
    return json.dumps({'@context': 'https://schema.org', '@graph': [
        {'@type': 'MedicalClinic', '@id': DOMAIN + '/#clinic', 'name': 'Nature’s Cure Wellness & Regimen Therapy Centre', 'alternateName': 'Nature’s Cure', 'url': DOMAIN + '/', 'telephone': '+919412276843', 'email': EMAIL, 'address': address, 'hasMap': MAP, 'areaServed': {'@type': 'City', 'name': 'Aligarh'}, 'description': 'Unani and regimenal therapy consultation with Dr. Mohammad Muhiul Haque Siddiqui in Greenpark, Manjur Garhi, Aligarh.'},
        {'@type': 'Person', '@id': DOMAIN + '/#doctor', 'name': 'Mohammad Muhiul Haque Siddiqui', 'honorificPrefix': 'Dr.', 'url': DOMAIN + '/doctor.html', 'hasCredential': [
            {'@type': 'EducationalOccupationalCredential', 'name': 'BUMMS'},
            {'@type': 'EducationalOccupationalCredential', 'name': 'M.D. (Ilmul Advia)'},
            {'@type': 'EducationalOccupationalCredential', 'name': 'M.D. (Moalejat)'}], 'alumniOf': {'@type': 'CollegeOrUniversity', 'name': 'Aligarh Muslim University'}, 'affiliation': {'@id': DOMAIN + '/#clinic'}},
        {'@type': 'WebSite', '@id': DOMAIN + '/#website', 'url': DOMAIN + '/', 'name': 'Nature’s Cure', 'publisher': {'@id': DOMAIN + '/#clinic'}},
        {'@type': 'WebPage', '@id': url + '#webpage', 'url': url, 'name': title, 'description': description, 'isPartOf': {'@id': DOMAIN + '/#website'}, 'about': {'@id': DOMAIN + '/#clinic'}, 'inLanguage': 'en-IN'}
    ]}, ensure_ascii=False, indent=2)

PAGES = {}
PAGES['index.html'] = ('Unani Doctor in Aligarh | Dr. M. M. H. Siddiqui | Nature’s Cure', 'Visit Nature’s Cure in Greenpark, Manjur Garhi, Aligarh for Unani and regimenal therapy consultation with Dr. Mohammad Muhiul Haque Siddiqui. Call +91 94122 76843.', f'''
<section class="hero recognition-hero"><div class="container"><div class="hero-grid"><div class="hero-identity"><span class="eyebrow">Unani consultation in Aligarh</span><h1><span class="hero-name-prefix">Prof. Dr.</span>Mohammad Muhiul<br>Haque Siddiqui</h1><p class="hero-qualifications">BUMMS · M.D. (Ilmul Advia) · M.D. (Moalejat)</p></div><figure class="hero-portrait-wrap"><img class="hero-portrait" src="images/mmh_siddiqui3.png" width="1122" height="1402" alt="Prof. Dr. Mohammad Muhiul Haque Siddiqui" fetchpriority="high" loading="eager"><figcaption><strong>Former Professor &amp; Dean</strong><span>Faculty of Unani Medicine · Aligarh Muslim University</span></figcaption></figure><div class="hero-content"><p class="hero-tagline">Rooted in tradition. Centred on you.</p><p class="intro">Unani medicine and regimenal therapy consultation at Nature’s Cure Wellness &amp; Regimen Therapy Centre, Aligarh.</p><div class="button-row">{button('Call for a consultation', glyph='phone')}{button('Meet the doctor', 'doctor.html', 'outline')}</div><p class="hero-note">{icon('pin')}Greenpark, Manjur Garhi · Aligarh, Uttar Pradesh</p></div></div><div class="trust-strip"><div class="trust-item">{icon('book')}<div><strong>Two postgraduate qualifications</strong><small>M.D. (Ilmul Advia) &amp; M.D. (Moalejat)</small></div></div><div class="trust-item">{icon('leaf')}<div><strong>A focus on regimenal therapy</strong><small>Ilaj-bit-Tadbeer</small></div></div><div class="trust-item">{icon('pin')}<div><strong>Here in your neighbourhood</strong><small>Behind ACN Ayurvedic Hospital, Aligarh</small></div></div></div></div></section>
<section class="section" id="care"><div class="container"><div class="section-head"><div><span class="eyebrow">An approach built around you</span><h2>Understanding comes<br>before a care plan.</h2></div><p>At our Unani clinic in Greenpark, Manjur Garhi, discuss your concerns and explore regimenal therapy with Dr. Siddiqui.</p></div><div class="cards"><article class="care-card"><div class="card-icon">{icon('leaf')}</div><h3>Unani medicine</h3><p>A consultation informed by Dr. Siddiqui’s academic and clinical background in Ilmul Advia and Moalejat.</p>{text_link('Explore the approach', 'care.html#unani')}</article><article class="care-card"><div class="card-icon">{icon('heart')}</div><h3>Regimenal therapy</h3><p>Discuss Ilaj-bit-Tadbeer, Dr. Siddiqui’s area of focus, and whether this approach may be appropriate for your circumstances.</p>{text_link('About Ilaj-bit-Tadbeer', 'care.html#regimenal')}</article><article class="care-card"><div class="card-icon">{icon('person')}</div><h3>A considered first visit</h3><p>Bring your questions and relevant medical records. Call ahead to discuss your visit and confirm availability.</p>{text_link('Plan your consultation', 'contact.html')}</article></div></div></section>
<section class="section" style="padding-top:20px"><div class="container doctor-feature">{portrait()}<div class="doctor-copy"><span class="eyebrow">Meet your doctor</span><h2>A career dedicated to<br>medicine &amp; learning.</h2><p class="credentials">Prof. Dr. Mohammad Muhiul Haque Siddiqui</p><p>Dr. Siddiqui’s career brings together teaching, research, and clinical practice in Unani medicine. An alumnus of Aligarh Muslim University, he has served as Professor and Chairman, with a particular focus on Ilaj-bit-Tadbeer.</p><div class="bio-facts"><div><strong>Since 1983</strong><small>A career in medical teaching</small></div><div><strong>AMU</strong><small>Alumnus &amp; former faculty member</small></div></div>{text_link('Read his background', 'doctor.html')}</div></div></section>
<section class="section soft-section"><div class="container"><div class="section-head"><div><span class="eyebrow">Your first steps</span><h2>A little preparation.<br>A clearer conversation.</h2></div><p>We’ll help you plan your visit to Nature’s Cure in Greenpark, Aligarh.</p></div><div class="steps"><article class="step"><span class="step-number">01 / GET IN TOUCH</span><h3>Start with a call</h3><p>Contact the clinic on {PHONE} to ask about a consultation and confirm timings.</p></article><article class="step"><span class="step-number">02 / COME PREPARED</span><h3>Bring your health history</h3><p>Have relevant reports and a list of current medicines ready to share during your consultation.</p></article><article class="step"><span class="step-number">03 / FIND US</span><h3>Visit us in Greenpark</h3><p>The clinic is behind ACN Ayurvedic Hospital, on Anoop Sheher Road in Manjur Garhi.</p></article></div></div></section>
{visit_banner()}
''')

PAGES['doctor.html'] = ('Dr. Mohammad Muhiul Haque Siddiqui, Aligarh | Nature’s Cure', 'Meet Dr. Mohammad Muhiul Haque Siddiqui, BUMMS, M.D. (Ilmul Advia), M.D. (Moalejat), former AMU Professor and Chairman, at Nature’s Cure in Aligarh.', f'''
{page_hero('The doctor', 'A lifetime of learning.<br>A thoughtful approach to care.', 'Meet Prof. Dr. Mohammad Muhiul Haque Siddiqui — Unani physician, educator, and former faculty member of Aligarh Muslim University.')}
<section class="page-section"><div class="container doctor-feature">{portrait()}<div class="doctor-copy"><span class="eyebrow">Experience &amp; perspective</span><h2>Prof. Dr. Mohammad<br>Muhiul Haque Siddiqui</h2><p class="credentials">BUMMS · M.D. (Ilmul Advia) · M.D. (Moalejat)</p><p>Dr. Siddiqui, also known as Prof. M. M. H. Siddiqui, has academic and clinical interests spanning Ilmul Advia, Moalejat, and Ilaj-bit-Tadbeer. His background includes teaching, postgraduate supervision, published research, and leadership in Unani medical education.</p><p>At Nature’s Cure in Aligarh, his focus is on consultation in Unani medicine and regimenal therapy.</p>{button('Enquire about a consultation', glyph='phone')}</div></div></section>
<section class="page-section"><div class="container bio-layout"><div class="prose"><h2>A connection to Aligarh</h2><p>Born in Lucknow in 1955, Dr. Siddiqui studied at S.T. High School (Minto Circle), Aligarh, before completing his medical education at Aligarh Muslim University. His association with the university has extended from school education to postgraduate study, teaching, and departmental leadership.</p><h2>Education &amp; academic career</h2><div class="timeline"><div class="timeline-item"><strong>1977 · Undergraduate qualification</strong><p>Completed BUMMS at Aligarh Muslim University, Aligarh.</p></div><div class="timeline-item"><strong>1983 · First postgraduate qualification</strong><p>Completed M.D. in Ilmul Advia. Began teaching at Rajasthan Unani Medical College, Jaipur, and subsequently served State Takmil-ut-Tib College, Lucknow, during 1983–1986.</p></div><div class="timeline-item"><strong>1986–1988 · Joining AMU faculty</strong><p>Joined the Department of Moalejat as a part-time Lecturer in 1986, becoming Lecturer in 1988.</p></div><div class="timeline-item"><strong>1996–2005 · Further study &amp; professorship</strong><p>Completed M.D. in Moalejat in 1996, became Reader in 1997, and Professor in 2005.</p></div><div class="timeline-item"><strong>2006–2009 · Departmental leadership</strong><p>Served as Chairman of the Department of Moalejat at Aligarh Muslim University.</p></div><div class="timeline-item"><strong>2011–2014 · Regimenal therapy</strong><p>Served as Chairman of the Department of Ilaj-bit-Tadbeer.</p></div><div class="timeline-item"><strong>2019–2020 · Faculty leadership</strong><p>Served as Dean, Faculty of Unani Medicine, Aligarh Muslim University.</p></div></div><h2>Teaching, research &amp; clinical interests</h2><p>His academic work includes postgraduate guidance, research publications, books, and contributions to conferences and professional education. His areas of interest include Ilmul Advia (pharmacology), Moalejat (clinical medicine), and Ilaj-bit-Tadbeer (regimenal therapy).</p><p>His particular focus is the study and development of regimenal therapy through academic work, research, and clinical practice.</p></div><aside class="side-note"><span class="eyebrow">At a glance</span><h3>Unani medicine.<br>An academic foundation.</h3><p><strong>Qualifications</strong><br>BUMMS<br>M.D. (Ilmul Advia)<br>M.D. (Moalejat)</p><p><strong>Academic background</strong><br>Former Professor, Chairman, and Dean at Aligarh Muslim University.</p><p><strong>Area of focus</strong><br>Ilaj-bit-Tadbeer (Regimenal Therapy).</p>{button('Contact the clinic', 'contact.html')}</aside></div></section>{visit_banner()}
''')

PAGES['care.html'] = ('Unani & Regimenal Therapy Consultation in Aligarh | Nature’s Cure', 'Learn about the consultation approach at Nature’s Cure, Aligarh, with a focus on Unani medicine and Ilaj-bit-Tadbeer under Dr. Mohammad Muhiul Haque Siddiqui.', f'''
{page_hero('Our approach', 'Care begins with<br>understanding.', 'Unani medicine and regimenal therapy consultation, informed by Dr. Siddiqui’s experience in teaching, research, and clinical practice.')}
<section class="page-section"><div class="container bio-layout"><div class="prose"><h2 id="unani">Unani medicine</h2><p>Nature’s Cure is a consultation clinic in Greenpark, Manjur Garhi, Aligarh, with a focus on Unani medicine. Dr. Siddiqui’s qualifications in Ilmul Advia and Moalejat provide the academic foundation for his work.</p><p>A consultation is an opportunity to discuss your health concerns, relevant medical history, and questions about the approach. Please contact the clinic to find out whether it is suitable for the concern you would like to discuss.</p><h2 id="regimenal">Ilaj-bit-Tadbeer</h2><p>Ilaj-bit-Tadbeer, also called regimenal therapy, is Dr. Siddiqui’s particular area of academic and clinical interest. His work has included the development of this discipline through teaching, research, and departmental leadership at Aligarh Muslim University.</p><p>Specific treatment options, their suitability, and any next steps should be discussed directly with the doctor during a consultation.</p><h2 id="prepare">Preparing for a consultation</h2><p>Call before visiting to confirm availability, timings, and consultation fees. Bring relevant medical reports, details of previous treatment, and a list of medicines or supplements you currently take.</p><p>Let the doctor know about any existing conditions, allergies, or ongoing care. Do not stop or change prescribed medicines without speaking to your treating clinician.</p></div><aside class="side-note"><span class="eyebrow">A conversation first</span><h3>Have a question<br>before you visit?</h3><p>Call the clinic to ask about consultation availability and whether your concern can be discussed with the doctor.</p>{button('Call ' + PHONE, glyph='phone')}<p>Nature’s Cure<br>Greenpark, Manjur Garhi<br>Aligarh, Uttar Pradesh</p></aside></div></section>
<section class="section soft-section"><div class="container"><div class="center"><span class="eyebrow">Useful to know</span><h2>Before your visit.</h2></div><div class="faq"><details><summary>How do I arrange a consultation?</summary><p>Call <a href="{TEL}">{PHONE}</a> to enquire about a consultation. Please confirm the date, time, and availability before travelling.</p></details><details><summary>What are the clinic’s opening hours?</summary><p>Please call the clinic to confirm current timings and the doctor’s availability.</p></details><details><summary>Where is Nature’s Cure located?</summary><p>{ADDRESS}. <a class="text-link" href="{MAP}">Open directions in Google Maps {icon('arrow')}</a></p></details><details><summary>What should I bring with me?</summary><p>Bring relevant test reports, records of previous treatment, and a list of any current medicines or supplements. Make a note of the questions you would like to ask.</p></details><details><summary>Can I get a diagnosis or treatment by email?</summary><p>The email address is for general enquiries. Diagnosis and treatment decisions require a consultation with the doctor. Please avoid sending sensitive medical documents by email.</p></details></div></div></section>{visit_banner()}
''')

PAGES['contact.html'] = ('Contact & Directions | Unani Clinic in Greenpark, Aligarh | Nature’s Cure', 'Call Nature’s Cure, Aligarh on +91 94122 76843. Find us on Anoop Sheher Road, behind ACN Ayurvedic Hospital, Greenpark, Manjur Garhi, Uttar Pradesh 202001.', f'''
{page_hero('Visit & contact', 'Your next step<br>starts here.', 'Get in touch with Nature’s Cure to enquire about a consultation with Dr. Mohammad Muhiul Haque Siddiqui in Aligarh.')}
<section class="page-section"><div class="container contact-grid"><div class="contact-card"><h2>Contact the clinic</h2><div class="detail">{icon('phone')}<div><small>Call for a consultation</small><a href="{TEL}">{PHONE}</a></div></div><div class="detail">{icon('mail')}<div><small>General enquiries</small><a href="mailto:{EMAIL}">{EMAIL}</a></div></div><div class="detail">{icon('pin')}<div><small>Clinic address</small><p>{ADDRESS}</p></div></div><div class="detail">{icon('clock')}<div><small>Timings &amp; availability</small><p>Please call before visiting to confirm clinic timings, consultation fees, and availability.</p></div></div>{button('Call the clinic', glyph='phone')}</div><div class="location-card"><div class="location-art" aria-hidden="true">{icon('pin')}</div><div><span class="eyebrow">Greenpark · Manjur Garhi</span><h3>Find us in Aligarh.</h3><p>Behind ACN Ayurvedic Hospital, on Anoop Sheher Road. Open Google Maps to plan your route to the supplied clinic address.</p>{button('Open Google Maps', MAP)}</div></div></div></section>
<section class="page-section"><div class="container"><div class="section-head"><div><span class="eyebrow">Plan ahead</span><h2>Make the most<br>of your visit.</h2></div><p>A call before you travel helps confirm the details and makes your visit easier to plan.</p></div><div class="cards"><article class="care-card"><div class="card-icon">{icon('clock')}</div><h3>Confirm your visit</h3><p>Ask about consultation availability, timings, and fees before coming to the clinic.</p></article><article class="care-card"><div class="card-icon">{icon('book')}</div><h3>Bring relevant records</h3><p>Have your previous reports and a list of current medicines ready for the consultation.</p></article><article class="care-card"><div class="card-icon">{icon('mail')}</div><h3>Keep enquiries general</h3><p>Use email for general questions. Please avoid sending sensitive medical information or reports.</p></article></div></div></section>
''')

PAGES['404.html'] = ('Page not found | Nature’s Cure', 'Return to Nature’s Cure, Unani and regimenal therapy consultation in Aligarh.', f'<section class="error-page container"><span class="eyebrow" style="justify-content:center">404 · Page not found</span><h1>Let’s get you<br>back on the path.</h1><p>This page could not be found. Visit our homepage or call the clinic for assistance.</p>{button("Return to the homepage", DOMAIN + "/")}</section>')

NAV = [('index.html', 'Home', './'), ('doctor.html', 'The doctor', 'doctor.html'), ('care.html', 'Our approach', 'care.html'), ('contact.html', 'Visit & contact', 'contact.html')]

# Keep the confirmed schedule consistent in page content and search metadata.
for filename, (title, description, content) in list(PAGES.items()):
    content = content.replace('<small>Timings &amp; availability</small><p>Please call before visiting to confirm clinic timings, consultation fees, and availability.</p>', '<small>Clinic hours</small>' + HOURS + '<p>Please call ahead to confirm consultation availability and fees.</p>')
    content = content.replace('<p>Please call the clinic to confirm current timings and the doctor’s availability.</p>', HOURS + '<p>Please call ahead to confirm the doctor’s availability.</p>')
    content = content.replace('<small>Plan your visit</small><p>Please call to confirm availability.</p>', '<small>Clinic hours</small>' + HOURS)
    PAGES[filename] = (title, description, content)

for filename, (title, description, content) in PAGES.items():
    if filename == 'doctor.html':
        content = content.replace('images/mmh_siddiqui.png', 'images/mmh_siddiqui2.png')
        content = content.replace('<aside class="side-note">', '<aside class="side-note"><img class="sidebar-portrait" src="images/mmh_siddiqui4.png" width="1122" height="1402" alt="Portrait of Dr. Mohammad Muhiul Haque Siddiqui in a blue jacket" loading="lazy">')
    canonical = DOMAIN + ('/' if filename == 'index.html' else '/' + filename)
    nav = ''.join(f'<a href="{href}"' + (' aria-current="page"' if filename == key else '') + f'>{label.replace("&", "&amp;")}</a>' for key, label, href in NAV)
    # Absolute assets on the custom domain let GitHub's 404 render at nested URLs.
    asset_prefix = DOMAIN + '/' if filename == '404.html' else ''
    robots = 'noindex, follow' if filename == '404.html' else 'index, follow, max-image-preview:large'
    structured_data = json.loads(schema(filename, title, description))
    structured_data['@graph'][0]['openingHoursSpecification'] = HOURS_SCHEMA
    structured_data['@graph'][0]['logo'] = DOMAIN + '/assets/clinic-logo.png'
    structured_data['@graph'][1]['image'] = DOMAIN + '/images/mmh_siddiqui.png'
    structured_data['@graph'][1]['alternateName'] = ['Prof. M. M. H. Siddiqui', 'Dr. M. M. H. Siddiqui']
    structured_data['@graph'][1]['knowsAbout'] = ['Unani medicine', 'Ilmul Advia (Pharmacology)', 'Moalejat (Clinical Medicine)', 'Ilaj-bit-Tadbeer (Regimenal Therapy)']
    structured_json = json.dumps(structured_data, ensure_ascii=False, indent=2)
    output = f'''<!doctype html>
<html lang="en-IN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>{escape(title)}</title><meta name="description" content="{escape(description, quote=True)}"><meta name="robots" content="{robots}"><meta name="theme-color" content="#173d32"><link rel="canonical" href="{canonical}"><meta property="og:type" content="website"><meta property="og:locale" content="en_IN"><meta property="og:site_name" content="Nature’s Cure"><meta property="og:title" content="{escape(title, quote=True)}"><meta property="og:description" content="{escape(description, quote=True)}"><meta property="og:url" content="{canonical}"><meta property="og:image" content="{DOMAIN}/images/mmh_siddiqui.png"><meta property="og:image:alt" content="Prof. Dr. Mohammad Muhiul Haque Siddiqui"><meta name="twitter:card" content="summary"><meta name="twitter:title" content="{escape(title, quote=True)}"><meta name="twitter:description" content="{escape(description, quote=True)}"><link rel="icon" type="image/svg+xml" href="{asset_prefix}assets/favicon.svg"><link rel="stylesheet" href="{asset_prefix}assets/styles.css"><script defer src="{asset_prefix}assets/site.js"></script><script type="application/ld+json">{structured_json}</script></head>
<body><a class="skip-link" href="#main">Skip to content</a><div class="topbar">Unani &amp; regimenal therapy consultation in Aligarh <span aria-hidden="true">&nbsp;·&nbsp;</span> <a href="{TEL}">Call {PHONE}</a></div><header class="site-header"><div class="container header-inner">{brand()}<button class="menu-button" type="button" aria-label="Open navigation" aria-expanded="false" aria-controls="main-navigation">{icon('menu')}</button><nav class="navigation" id="main-navigation" aria-label="Main navigation">{nav}</nav><a class="button header-call" href="{TEL}">{icon('phone')}Call the clinic</a></div></header>
<main id="main">{content}</main>
<footer class="site-footer"><div class="container"><div class="footer-main"><div>{brand()}<p>Unani medicine &amp; regimenal therapy consultation.<br>Greenpark, Manjur Garhi, Aligarh.</p></div><nav class="footer-links" aria-label="Footer navigation"><a href="doctor.html">The doctor</a><a href="care.html">Our approach</a><a href="contact.html">Visit &amp; contact</a><a href="mailto:{EMAIL}">Email us {icon('arrow')}</a></nav></div><div class="footer-bottom"><span>© 2026 Nature’s Cure · Aligarh, India</span><p>This website provides general clinic information. Medical advice and treatment decisions require a consultation.</p></div></div></footer><a class="button mobile-call" href="{TEL}">{icon('phone')}Call for a consultation<span aria-hidden="true">↗</span></a></body></html>'''
    if filename == '404.html':
        output = output.replace('href="assets/', f'href="{DOMAIN}/assets/').replace('src="assets/', f'src="{DOMAIN}/assets/')
        output = output.replace('href="./"', f'href="{DOMAIN}/"')
        for target in ('doctor.html', 'care.html', 'contact.html'):
            output = output.replace(f'href="{target}"', f'href="{DOMAIN}/{target}"')
    output = output.replace('assets/favicon.svg', 'assets/clinic-logo.png').replace('type="image/svg+xml"', 'type="image/png"')
    (ROOT / filename).write_text(output, encoding='utf-8')

sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
for filename in PAGES:
    if filename != '404.html':
        sitemap += f'  <url><loc>{DOMAIN}{"/" if filename == "index.html" else "/" + filename}</loc></url>\n'
(ROOT / 'sitemap.xml').write_text(sitemap + '</urlset>\n', encoding='utf-8')
(ROOT / 'robots.txt').write_text(f'User-agent: *\nAllow: /\n\nSitemap: {DOMAIN}/sitemap.xml\n', encoding='utf-8')
print(f'Generated {len(PAGES)} HTML pages, sitemap.xml, and robots.txt.')
