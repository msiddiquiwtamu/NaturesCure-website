# Nature’s Cure — Aligarh

A responsive static website for Unani and regimenal therapy consultation with Dr. Mohammad Muhiul Haque Siddiqui. Designed for GitHub Pages; no installation, build service, backend, or API key is needed.

## Preview

From this folder, run `python -m http.server 8000 --bind 127.0.0.1`, then open `http://127.0.0.1:8000`.

## Content and styling

- `tools/build_site.py` contains the page content, shared layout, contact details, and structured data. Run `python tools/build_site.py` after editing it to regenerate HTML, sitemap, and robots.txt.
- `assets/styles.css` contains responsive styles; `assets/site.js` handles the mobile navigation.
- All four doctor portraits in `images/` were supplied by the clinic owner. The newest formal portrait appears in the homepage opening section, with a prominent name; the other new portrait appears alongside the doctor’s biography. The original portraits remain in the doctor introduction sections.
- `assets/garden.svg` is an original decorative botanical illustration, not a photograph of the clinic.
- Google Fonts is optional; system fonts are used if it is unavailable. There are no analytics, forms, embedded maps, or patient data storage.

## Publishing to GitHub Pages

The site is ready for a repository published from `main`, `/(root)`. Push these files to the clinic’s repository, then enable GitHub Pages in its settings. The included `CNAME` sets the intended custom domain to `naturescures.in`; DNS must also be configured before that domain serves this site. Nothing in this project changes DNS automatically.

See [GitHub’s custom domain instructions](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site). Enable HTTPS once GitHub provisions the certificate. Canonicals and sitemap URLs use `https://naturescures.in/`.

## Search visibility

Included: unique page titles and descriptions, canonical URLs, social metadata, semantic headings, clinic/person structured data, a four-page sitemap, robots.txt, and a custom 404. Address, telephone, and location copy are consistent across the site.

After deployment, verify the domain in Google Search Console and submit `https://naturescures.in/sitemap.xml`. Review the existing Google Business Profile: the supplied screenshot shows “Temporarily closed” and a different displayed name. Confirm current operating status and the official business name with the owner before updating that profile. Check its address, phone number, and website against the final confirmed details. Website changes alone do not update Google Maps.

Google’s [SEO starter guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide) and [local business structured data documentation](https://developers.google.com/search/docs/appearance/structured-data/local-business) describe the search features used here. Indexing and ranking are determined by search engines and are not guaranteed.

## Details to add when confirmed

Consultation fees, precise appointment arrangements, specific available therapies and genuine clinic photos. Historical university roles are identified as former roles. No testimonials, treatment outcomes, ratings, or unconfirmed procedures are fabricated.

Confirmed hours (IST): Monday–Thursday 10:00 am–5:00 pm; Friday closed; Saturday–Sunday 10:00 am–2:00 pm. Visible hours and structured data are maintained together in `tools/build_site.py`.

Confirmed clinic name from its sign: **Nature’s Cure Wellness & Regimen Therapy Centre**. Domain: **naturescures.in** (plural, intentionally different from the clinic name). The sign’s older opening hours are superseded by the owner’s confirmed schedule above.
