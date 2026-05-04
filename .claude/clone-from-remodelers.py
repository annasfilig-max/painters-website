"""Clone remodelers-website -> painters-website
 - jsDelivr repo URL: remodelers-website -> painters-website
 - Image extensions: .png stays .png (both use png)
 - Navy accent (#4870A8) -> light blue (#5DADE2)
 - Kitchen/bath service content -> painter service content
"""
import os, re, shutil

REM = os.path.expanduser('~/Downloads/Claude/remodelers-website')
DST = os.path.expanduser('~/Downloads/Claude/painters-website')

PAGES = ['index.html','about.html','services.html','service-areas.html',
         'gallery.html','testimonials.html','faq.html','contact.html',
         'quote.html','privacy.html','terms.html','404.html']

# 1. Recolor CSS
with open(os.path.join(REM, 'assets/css/styles.css'), encoding='utf-8') as f:
    css = f.read()

css = css.replace('REMODELERS — Dark Premium + Brass Accent',
                  'PAINTERS — Dark Premium + Light Blue')
css = css.replace('warm brass accent (kitchen/bath fixtures)',
                  'light blue accent (painter trade)')
css = css.replace('--brass:        #4870A8', '--brass:        #5DADE2')
css = css.replace('--brass-bright: #6090C8', '--brass-bright: #7FBFE8')
css = css.replace('--brass-deep:   #2D4F7E', '--brass-deep:   #3A8AB8')
css = css.replace('rgba(72, 112, 168, 0.5)',  'rgba(93, 173, 226, 0.5)')
css = css.replace('rgba(72, 112, 168, 0.1)',  'rgba(93, 173, 226, 0.1)')
css = css.replace('rgba(72, 112, 168, 0.45)', 'rgba(93, 173, 226, 0.45)')
css = css.replace('rgba(72, 112, 168, 0.3)',  'rgba(93, 173, 226, 0.3)')
css = css.replace('rgba(72, 112, 168, 0.04) 1px',
                  'rgba(93, 173, 226, 0.04) 1px')
css = css.replace('rgba(96, 144, 200, 0.32)', 'rgba(127, 191, 232, 0.32)')
css = css.replace('#9DC0E8', '#B8DBF0')
css = css.replace('annasfilig-max/remodelers-website',
                  'annasfilig-max/painters-website')
css = css.replace('#4870A8', '#5DADE2')

with open(os.path.join(DST, 'assets/css/styles.css'), 'w', encoding='utf-8', newline='\n') as f:
    f.write(css)
print('  CSS copied + navy -> light blue #5DADE2')

# 2. Copy main.js verbatim
shutil.copy(os.path.join(REM, 'assets/js/main.js'),
            os.path.join(DST, 'assets/js/main.js'))
print('  main.js copied')

# 3. HTML content swaps
SWAPS = [
    # repo URL
    ('annasfilig-max/remodelers-website', 'annasfilig-max/painters-website'),
    # tagline
    ('Kitchen &amp; Bath Remodels', 'Interior &amp; Exterior Painting'),
    ('Kitchen &middot; Bath &middot; Whole-Home Remodels',
     'Interior &middot; Exterior &middot; Cabinet Refinishing'),
    # SEO
    ('Kitchen &amp; Bath Remodelers in [City, State]',
     'Painters in [City, State]'),
    ('design-build kitchen and bath remodelers',
     'professional residential painters'),
    ('Custom cabinetry, countertops, tile, and full renovations.',
     'Interior, exterior, cabinet refinishing, drywall, trim &mdash; quotes in 48 hours.'),
    ('Remodels Done Right', 'Painting Done Right'),
    ('Design-build kitchen and bath remodels by a local crew that finishes on time and on budget.',
     'Walls prepped right, lines crisp, mess gone &mdash; finished on the day we said.'),
    # Nav label
    ('<a href="/gallery">Portfolio</a>',
     '<a href="/gallery">Portfolio</a>'),
    # Hero
    ('Kitchens &amp; Baths<br><em>Built To Last.</em>',
     'Color That<br><em>Holds Up.</em>'),
    ("Design-build remodels by a local crew that doesn't ghost mid-project. Measured, designed, built, and warrantied &mdash; start to reveal in one trade.",
     "Interior, exterior, cabinet, drywall &mdash; one painter-led crew, prepped right, lines straight, every drop cloth folded before we leave."),
    ('Book a Design Visit', 'Get a Free Quote'),
    ('View Portfolio', 'Call [Phone Number]'),
    ('Years Building', 'Years Painting'),
    ('Rooms Done', 'Rooms Painted'),
    ('Houzz / Google', 'Avg Google'),
    ('Featured Build<br>[Project Name]', 'Featured Job<br>[Project Name]'),
    # Marquee
    ('NKBA Member Designers', 'PCA Member Painters'),
    ('NARI Certified Builders', 'EPA Lead-Safe Certified'),
    ('Free In-Home Design Visits', 'Free On-Site Color Consult'),
    ('15-Year Workmanship Warranty', '5-Year Workmanship Warranty'),
    ('Lead-Safe EPA RRP Certified', 'Bonded &amp; Insured'),
    ('On-Time, On-Budget', 'Sherwin-Williams &amp; Benjamin Moore'),
    # Services section header
    ('Six Specialties.<br>One Crew On Site.',
     'Six Services.<br>One Crew. One Standard.'),
    ('Design + Build, In-House', 'Prep &middot; Paint &middot; Cleanup'),
    # Slug anchors
    ('href="/services#kitchen"', 'href="/services#interior"'),
    ('href="/services#bath"', 'href="/services#exterior"'),
    ('href="/services#cabinets"', 'href="/services#cabinet-paint"'),
    ('href="/services#counters"', 'href="/services#drywall"'),
    ('href="/services#tile"', 'href="/services#trim"'),
    ('href="/services#design"', 'href="/services#color"'),
    ('id="kitchen"',  'id="interior"'),
    ('id="bath"',     'id="exterior"'),
    ('id="cabinets"', 'id="cabinet-paint"'),
    ('id="counters"', 'id="drywall"'),
    ('id="tile"',     'id="trim"'),
    ('id="design"',   'id="color"'),
    # Service card titles
    ('01 / Signature</span>\n          <h3>Kitchen Remodels</h3>',
     '01 / Interior</span>\n          <h3>Interior Painting</h3>'),
    ('02 / Signature</span>\n          <h3>Bath Remodels</h3>',
     '02 / Exterior</span>\n          <h3>Exterior Painting</h3>'),
    ('03 / Cabinetry</span>\n          <h3>Cabinets &amp; Refacing</h3>',
     '03 / Cabinets</span>\n          <h3>Cabinet Refinishing</h3>'),
    ('04 / Surfaces</span>\n          <h3>Countertops &amp; Stone</h3>',
     '04 / Repair</span>\n          <h3>Drywall &amp; Patching</h3>'),
    ('05 / Tile</span>\n          <h3>Custom Tile &amp; Stone</h3>',
     '05 / Trim</span>\n          <h3>Trim, Doors &amp; Wallpaper</h3>'),
    ('06 / Design</span>\n          <h3>Design Consultation</h3>',
     '06 / Consult</span>\n          <h3>Color Consultation</h3>'),
    # Card descriptions
    ('Full-gut to refresh. Cabinets, counters, lighting, flooring &mdash; one crew, one timeline, one warranty.',
     'Walls, ceilings, trim, doors. Tinted Sherwin-Williams or Benjamin Moore &mdash; cut lines, no roller marks.'),
    ('Spa-grade primary baths to clean second-bath refreshes. Tile, plumbing, vanities, glass &mdash; in-house.',
     'Siding, trim, decks, fences. Power-wash, scrape, prime, two coats &mdash; built to handle weather.'),
    ('Custom, semi-custom, or refacing. Tight joinery, real wood, finishes that hold &mdash; sized and installed in-house.',
     'Sand, prime, sprayed lacquer or enamel finish. Looks factory-new &mdash; for a quarter the cost of replacement.'),
    ('Quartz, granite, marble, butcher block. Templated, fabricated, installed &mdash; without the markup games.',
     'Patch, skim-coat, texture-match, paint. Holes, cracks, water damage &mdash; you won\'t see where it was.'),
    ('Backsplashes, shower walls, floors. Hand-laid by tile specialists &mdash; not the lowest-bid sub.',
     'Crown, baseboards, doors, casings. Wallpaper removal or install &mdash; clean lines, no bubbles.'),
    ('3D visualization, material selection, and an honest budget &mdash; before any demo starts.',
     'Stuck on a color? In-home consult with samples and good lighting advice &mdash; no commitment.'),
    ('Explore Kitchens &rarr;', 'Interior Details &rarr;'),
    ('Explore Baths &rarr;',    'Exterior Details &rarr;'),
    ('See Cabinetry &rarr;',    'Cabinet Refinishing &rarr;'),
    ('See Surfaces &rarr;',     'Drywall Details &rarr;'),
    ('See Tile Work &rarr;',    'Trim &amp; Wallpaper &rarr;'),
    ('Book a Design Visit &rarr;', 'Color Consultation &rarr;'),
    # Portfolio
    ('Recent<br>Transformations.', 'Recent Jobs.<br>Real Rooms.'),
    ('[##]+ Builds Delivered', '4,800+ Rooms Painted'),
    ('Kitchen', 'Interior'),
    ('Primary Bath', 'Exterior'),
    ('Cabinetry', 'Cabinets'),
    ('Custom Tile', 'Drywall'),
    ('Open-Plan', 'Trim'),
    ('Powder Room', 'Color Match'),
    ('Quartz Counters', 'Spray Finish'),
    ('See Full Portfolio &rarr;', 'See Full Portfolio &rarr;'),
    # About
    ('A Crew That<br>Treats Your Home<br>Like Their Own.',
     'A Crew That<br>Treats Your Walls<br>Like Their Own.'),
    ("Family-owned since [Year]. Built on the idea that homeowners shouldn't have to be afraid of contractors &mdash; no mystery invoices, no high-pressure sales, no leaving you on hold for three weeks while we finish someone else's job.",
     "Family-owned since [Year]. Built on the idea that homeowners shouldn't have to dread the painter showing up &mdash; no over-spray on the floor, no roller marks on the ceiling, no \"we'll come back tomorrow\" for two weeks."),
    ('Background-checked, drug-tested crew', 'Background-checked, drug-tested painters'),
    ('Fixed-price quotes &mdash; the invoice matches the quote', 'Flat-rate quotes &mdash; the invoice matches the quote'),
    ('Floors covered, daily cleanup, debris hauled', 'Drop cloths over everything, daily cleanup, never any over-spray'),
    ('15-year workmanship warranty on every job', '5-year workmanship warranty on every job'),
    # Process
    ('Sketch.<br>Build. Reveal.', 'Quote.<br>Prep. Paint.'),
    ('Discovery Call', 'On-Site Quote'),
    ('15 minutes on the phone &mdash; scope, ballpark budget, and whether we\'re a fit.',
     'Walk the rooms, count the doors, talk colors &mdash; flat-rate quote on the spot.'),
    ('Design &amp; Quote', 'Prep &amp; Protect'),
    ('In-home measure, 3D plans, material selections, fixed-price quote &mdash; before any demo.',
     'Move furniture to the middle, drop cloths everywhere, tape, sand, patch &mdash; the boring 60% that makes the paint last.'),
    ('Build It Right', 'Paint It Right'),
    ('Code-correct framing, plumbing, electrical, finishing &mdash; daily updates, no ghosts.',
     'Premium primer, two coats, cut-line by hand, brush-quality on trim &mdash; no shortcuts that show up in 6 months.'),
    ('Reveal &amp; Warranty', 'Final Walk'),
    ('Walkthrough, punch list, 15-year workmanship warranty, clean job site at handoff.',
     'Walk every room with you under good light. Touch-ups same day. 5-year workmanship warranty.'),
    # Big quote
    ('Quoted in week one, demoed in week three, finished in week six &mdash; all within a hundred bucks of the original number. Every contractor we\'d hired before would have laughed at this kind of timeline. They actually delivered.',
     "Painted our entire 4-bedroom in 4 days. Cut lines were perfect, no over-spray on the floor or ceilings, and they touched up everything we pointed out the next morning. The price was the price. Could not recommend more."),
    ('Full Kitchen Remodel &middot; [City]', 'Full Interior Repaint &middot; [City]'),
    ('Janet &amp; David M.', 'Janet M.'),
    # Service areas
    ('Where We Build.', 'Where We Paint.'),
    # CTA
    ('Ready To<br><em>Sketch It?</em>', 'Ready For<br><em>Fresh Walls?</em>'),
    ('Free in-home design visit. Fixed-price quote within five business days. No high-pressure sales script &mdash; just an honest scope and number.',
     'Free in-home quote. Flat-rate price within 48 hours. No high-pressure sales pitch &mdash; just an honest scope, color guidance, and a real timeline.'),
    # Form
    ('Full kitchen remodel', 'Interior painting'),
    ('Full bath remodel', 'Exterior painting'),
    ('Cabinets / refacing', 'Cabinet refinishing'),
    ('Countertops / surfaces', 'Drywall repair / patching'),
    ('Custom tile work', 'Trim / doors / wallpaper'),
    ('Design consultation only', 'Color consultation only'),
    ('Whole-home renovation', 'Whole-home repaint'),
    ("Square footage, age of home, what you're hoping to change&hellip;",
     "Number of rooms, ceiling height, color ideas&hellip;"),
    # Footer
    ('Specialties', 'Services'),
    ('Kitchen Remodels', 'Interior Painting'),
    ('Bath Remodels', 'Exterior Painting'),
    ('Cabinets &amp; Refacing', 'Cabinet Refinishing'),
    ('Countertops', 'Drywall &amp; Patching'),
    ('Custom Tile', 'Trim &amp; Wallpaper'),
    ('Design Consultation', 'Color Consultation'),
    ('Mon&ndash;Fri 8a&ndash;6p<br>Free In-Home Design Visits',
     'Mon&ndash;Fri 7a&ndash;5p &middot; Sat By Appt<br>Free In-Home Color Consults'),
    ('Design-build remodelers serving [Service Region]. Fixed-price quotes, real timelines, and a 15-year workmanship warranty on every job.',
     'Family-owned painting company serving [Service Region]. Flat-rate quotes, clean prep, and a 5-year workmanship warranty on every job.'),
    # Social
    ('aria-label="Houzz"', 'aria-label="Google"'),
    # Schema type
    ('"@type": "GeneralContractor"', '"@type": "LocalBusiness"'),
]

for p in PAGES:
    src = os.path.join(REM, p)
    dst = os.path.join(DST, p)
    with open(src, encoding='utf-8') as fh: html = fh.read()
    for old, new in SWAPS:
        html = html.replace(old, new)
    with open(dst, 'w', encoding='utf-8', newline='\n') as fh: fh.write(html)
    print(f'  built {p:25s}  {len(html):6d}b')

# Sitemap
with open(os.path.join(DST, 'sitemap.xml'), 'w', encoding='utf-8', newline='\n') as fh:
    fh.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
             ''.join(f'  <url><loc>[https://yourdomain.com]/{p}</loc><lastmod>2026-05-03</lastmod><changefreq>monthly</changefreq><priority>{pri}</priority></url>\n'
                     for p, pri in [('index.html','1.0'),('about.html','0.8'),('services.html','0.9'),
                                    ('service-areas.html','0.8'),('gallery.html','0.7'),
                                    ('testimonials.html','0.7'),('faq.html','0.7'),
                                    ('contact.html','0.9'),('quote.html','0.9'),
                                    ('privacy.html','0.3'),('terms.html','0.3')]) +
             '</urlset>\n')

# Delete blog
import shutil as sh
for f in ['blog.html']:
    p = os.path.join(DST, f)
    if os.path.exists(p): os.remove(p); print(f'  deleted {f}')
blogdir = os.path.join(DST, 'blog')
if os.path.isdir(blogdir): sh.rmtree(blogdir); print('  deleted blog/')
print('\nDone.')
