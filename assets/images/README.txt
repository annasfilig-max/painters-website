IMAGE REPLACEMENT GUIDE
=======================

Below is every placeholder image in the site. Replace each URL with your own
photo at (or close to) the specified dimensions for best results. All current
placeholders are served from https://placehold.co — search your HTML files
for "placehold.co" to find every slot fast.

Tip: save your replacement photos inside this folder (assets/images/) and
reference them with a relative path, e.g. src="assets/images/hero.jpg".


HOME PAGE  (index.html)
-----------------------
- Hero background (1920x1080) — wide, bright shot: freshly painted living room,
  exterior repaint, or a painter mid-brushstroke. Avoid busy backgrounds — the
  headline sits on top. Use a warm, hopeful tone.
- "Why Choose Us" section image (800x600) — team on a real job site, crew
  carrying ladders, or a finished interior. People photos convert better than
  product shots.
- Service area teaser map (600x400) — screenshot of a map showing your
  coverage region, or a stylized map illustration.
- 3x Recent blog preview cards (600x400 each) — same images as the blog
  featured posts below.


ABOUT PAGE  (about.html)
------------------------
- Our Story image (700x500) — owner or crew on-site, founder portrait,
  company truck, or a signature finished project.
- 4x Team photos (400x400 each) — head-and-shoulders portraits, consistent
  background, neutral expressions. Square crops.
- 6x Certification / affiliation logos (200x100 each, transparent PNG) —
  BBB, PDCA, manufacturer partnerships, Chamber of Commerce, local
  associations. Display grayscale.


SERVICES PAGE  (services.html)
------------------------------
- 6x Service section images (700x500 each) — one representative photo per
  service. Before/after splits work well here; in-progress shots with a
  crew member beat empty-room shots every time.


SERVICE AREAS PAGE  (service-areas.html)
----------------------------------------
- Coverage map (1200x675, 16:9 aspect) — regional map with your service
  footprint highlighted. Google Maps screenshot or custom illustration.


GALLERY PAGE  (gallery.html)
----------------------------
- 12x Project photos — mix of aspect ratios for masonry feel:
  600x600, 600x750, 600x800, 600x900. Show variety across services,
  interior + exterior, residential + commercial. High-res, bright,
  true-to-color.


TESTIMONIALS PAGE  (testimonials.html)
--------------------------------------
- No images required — uses initial-letter avatars. Optional: swap the
  avatar divs for real customer photos (circular, 80x80) if you have
  signed permission.


BLOG PAGE  (blog.html)
----------------------
- Featured post image (800x500) — matches post-1 featured below.
- 2x Blog card images (600x400 each) — match post-2 and post-3
  featured images below.


BLOG POSTS  (blog/post-1.html, post-2.html, post-3.html)
--------------------------------------------------------
Each post needs:
- Featured image (1200x630) — wide, high-quality editorial shot
  relevant to the post topic.
- Inline figure (900x500) — supporting image placed roughly halfway
  through the article.

Post 1 — "Signs It's Time to Repaint"
  Featured: weathered exterior, faded siding, or peeling trim
  Inline:   interior wall detail showing scuffs near light switches

Post 2 — "How to Choose Colors That Add Value"
  Featured: color fan deck, swatches on a counter, or a styled
            paint-sampling shot
  Inline:   well-lit open-plan room with a cohesive neutral palette

Post 3 — "What to Look For When Hiring a Painting Contractor"
  Featured: homeowner + contractor reviewing a written quote
  Inline:   painter doing prep work (sanding, caulking, masking)


CONTACT PAGE  (contact.html)
----------------------------
- No images required. Google Maps iframe is commented out — follow the
  inline instructions in contact.html to paste your actual embed URL
  from Google Maps → Share → Embed a map.


QUOTE PAGE  (quote.html)
------------------------
- No images required.


404 PAGE  (404.html)
--------------------
- No images required. Uses an inline SVG illustration.


FAVICON
-------
- assets/favicon.svg — edit the SVG directly if you want to swap colors
  or the icon shape. A simple brushstroke or paint roller at 32x32 or
  64x64 will render crisply at all sizes.


SOCIAL / OPEN GRAPH IMAGES
--------------------------
Every HTML page has an <meta property="og:image"> tag. For best social
sharing results, create a 1200x630 branded image per page (company logo +
page title on a brand-colored background). Search each HTML file for
"og:image" to find every instance to update.


FORMSPREE
---------
All 3 forms (quote, contact, newsletter) POST to
https://formspree.io/f/YOUR_FORM_ID — replace YOUR_FORM_ID with your
actual Formspree endpoint. Search the HTML files for "YOUR_FORM_ID"
to find all occurrences.


PLACEHOLDERS
------------
Every business-specific detail is wrapped in square brackets for easy
find-and-replace. Work through these in your text editor:
  [Your Company Name]   [Phone Number]       [Email]
  [Street Address]      [City, State ZIP]    [Year Founded]
  [Year]                [License #]          [Service Region]
  [Author Name]         [City One]...[City Twelve]
  [State]               [Effective Date]
  [XX], [XXX], [XXXX]   (stats — years, reviews, jobs, etc.)
