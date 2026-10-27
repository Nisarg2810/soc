"""Builds the static site into the repository root.

    python3 tools/build.py

Edit tools/config.py (business details) and tools/content.py (projects, services, articles).
"""
import json
import html
from datetime import date
from pathlib import Path

import config as C
from content import PROJECTS, PROJECT_CATS, SERVICES, PROCESS, MATERIALS, HOME_FAQS, ARTICLES

ROOT = Path(__file__).resolve().parent.parent
IMG = json.loads((Path(__file__).parent / "img_idx.json").read_text())
TODAY = date.today().isoformat()
PAGES = []  # (path, lastmod, priority) for the sitemap

esc = html.escape


def u(path=""):
    """Site-relative URL."""
    return C.BASE + path


def abs_url(path=""):
    return C.SITE_URL + path


# ---------------------------------------------------------------- images
def src(key, w, ratio=None):
    pid = IMG[key]
    q = f"https://images.unsplash.com/photo-{pid}?auto=format&fit=crop&w={w}&q=72"
    if ratio:
        q += f"&h={round(w * ratio)}"
    return q


def img(key, alt, ratio=1.25, sizes="100vw", cls="", eager=False, widths=(480, 800, 1200, 1600, 2200)):
    srcset = ", ".join(f"{src(key, w, ratio)} {w}w" for w in widths)
    w0 = 1600
    h0 = round(w0 * ratio)
    attrs = 'loading="eager" fetchpriority="high"' if eager else 'loading="lazy"'
    c = f' class="{cls}"' if cls else ""
    return (f'<img{c} src="{src(key, 1200, ratio)}" srcset="{srcset}" sizes="{sizes}" '
            f'width="{w0}" height="{h0}" alt="{esc(alt)}" decoding="async" {attrs}>')


# ---------------------------------------------------------------- schema
def org_schema():
    s = {
        "@context": "https://schema.org",
        "@type": "HomeAndConstructionBusiness",
        "@id": abs_url("#business"),
        "name": C.NAME,
        "alternateName": C.SHORT,
        "description": C.TAGLINE + ". Modular kitchens, wardrobes, bespoke furniture and complete home and office interiors.",
        "url": abs_url(),
        "logo": abs_url("assets/img/icon-512.png"),
        "image": abs_url("assets/img/og-default.jpg"),
        "telephone": C.PHONE_E164,
        "email": C.EMAIL,
        "priceRange": "₹₹",
        "foundingDate": C.FOUNDED,
        "address": {
            "@type": "PostalAddress",
            "streetAddress": C.STREET,
            "addressLocality": f"{C.LOCALITY}, {C.CITY}",
            "addressRegion": C.REGION,
            "postalCode": C.POSTCODE,
            "addressCountry": C.COUNTRY,
        },
        "geo": {"@type": "GeoCoordinates", "latitude": C.LAT, "longitude": C.LNG},
        "hasMap": C.MAPS_URL,
        "openingHoursSpecification": [
            {"@type": "OpeningHoursSpecification", "dayOfWeek": h["days"], "opens": h["opens"], "closes": h["closes"]}
            for h in C.HOURS_SCHEMA
        ],
        "areaServed": [{"@type": "City", "name": "Ahmedabad"}, {"@type": "City", "name": "Gandhinagar"}],
        "knowsAbout": ["Interior design", "Modular kitchens", "Wardrobes", "Custom furniture", "Office interiors", "Home renovation"],
        "hasOfferCatalog": {
            "@type": "OfferCatalog",
            "name": "Interior design services",
            "itemListElement": [
                {"@type": "Offer", "itemOffered": {"@type": "Service", "name": s["name"], "url": abs_url(f"services/{s['slug']}/")}}
                for s in SERVICES
            ],
        },
    }
    same = [v for v in C.SOCIAL.values() if v]
    if same:
        s["sameAs"] = same
    return s


def website_schema():
    return {"@context": "https://schema.org", "@type": "WebSite", "@id": abs_url("#website"), "url": abs_url(),
            "name": C.NAME, "inLanguage": "en-IN", "publisher": {"@id": abs_url("#business")}}


def crumbs_schema(trail):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": name, "item": abs_url(path)} for i, (name, path) in enumerate(trail)]}


def faq_schema(faqs):
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]}


# ---------------------------------------------------------------- partials
MONO = (
    '<svg viewBox="100 288 760 250" aria-hidden="true" focusable="false"><g fill="none" stroke="currentColor" '
    'stroke-width="1.35" vector-effect="non-scaling-stroke" stroke-linecap="round" stroke-linejoin="round" transform="translate(0 18)">'
    '<path vector-effect="non-scaling-stroke" d="M 392 316 C 404 288, 370 268, 310 276 C 228 288, 176 322, 194 360 C 212 396, 322 398, 354 438 C 384 474, 344 507, 272 504 C 204 501, 150 480, 116 448"/>'
    '<path vector-effect="non-scaling-stroke" d="M 476 314 C 488 286, 522 276, 542 302 C 568 338, 566 444, 530 482 C 500 512, 454 492, 446 420 C 440 354, 466 290, 520 284"/>'
    '<path vector-effect="non-scaling-stroke" d="M 748 336 C 770 304, 742 280, 702 290 C 634 306, 596 376, 604 436 C 612 494, 680 512, 742 492 C 786 478, 816 452, 840 424"/>'
    '</g></svg>'
)
CHAT_ICON = ('<svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round">'
             '<path d="M20 11.5a8 8 0 0 1-11.8 7L4 20l1.5-4A8 8 0 1 1 20 11.5Z"/></svg>')

NAV = [("Projects", "projects/"), ("Services", "services/"), ("Studio", "studio/"), ("Journal", "journal/")]


def header(current):
    def link(label, path):
        cur = ' aria-current="page"' if current == path else ""
        return f'<a href="{u(path)}"{cur}>{label}</a>'
    left = "".join(link(l, p) for l, p in NAV)
    drawer = "".join(f'<li><a href="{u(p)}">{l}</a></li>' for l, p in NAV + [("Contact", "contact/")])
    return f'''<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <div class="wrap">
    <nav class="nav left" aria-label="Main">
      <button class="menu-btn" type="button" aria-expanded="false" aria-controls="drawer"><i></i><span class="label" style="color:inherit">Menu</span></button>
      {left}
    </nav>
    <a class="brand" href="{u()}" aria-label="{C.NAME} home">{MONO}<span>Shree Ohm Creation</span></a>
    <nav class="nav right" aria-label="Contact">
      <a href="tel:{C.PHONE_E164}">{C.PHONE_DISPLAY}</a>
      <a class="cta keep" href="{u('contact/')}">Book a visit</a>
      <a class="keep only-mobile" href="tel:{C.PHONE_E164}">Call</a>
    </nav>
  </div>
</header>
<div class="drawer" id="drawer">
  <ul>{drawer}</ul>
  <div class="drawer-foot">
    <a class="btn" href="{u('contact/')}">Book a free consultation</a>
    <span>{C.PHONE_DISPLAY} · {C.EMAIL}</span>
    <span>{C.LOCALITY}, {C.CITY}</span>
  </div>
</div>'''


def footer():
    svc = "".join(f'<li><a href="{u("services/" + s["slug"] + "/")}">{s["name"]}</a></li>' for s in SERVICES)
    social = [(k, v) for k, v in C.SOCIAL.items() if v]
    social_html = "".join(f'<li><a href="{v}" rel="noopener" target="_blank">{k}</a></li>' for k, v in social) or "<li>Instagram</li><li>Facebook</li><li>Pinterest</li>"
    return f'''<footer class="site-footer">
  <div class="wrap">
    <div class="foot-grid">
      <div class="foot-brand">
        <img src="{u('assets/img/logo-plaster.svg')}" width="150" height="150" alt="{C.NAME} Interiors logo" loading="lazy">
        <p>{C.TAGLINE}. Designed in our studio, made in our own workshop, installed by our own team.</p>
      </div>
      <div>
        <h2>Services</h2>
        <ul>{svc}</ul>
      </div>
      <div>
        <h2>Studio</h2>
        <ul>
          <li><a href="{u('projects/')}">Projects</a></li>
          <li><a href="{u('studio/')}">About us</a></li>
          <li><a href="{u('journal/')}">Journal</a></li>
          <li><a href="{u('contact/')}">Contact</a></li>
          {social_html}
        </ul>
      </div>
      <div>
        <h2>Visit</h2>
        <address>
          {C.NAME}<br>{C.STREET}<br>{C.LOCALITY}, {C.CITY}<br>{C.REGION} {C.POSTCODE}<br><br>
          <a href="tel:{C.PHONE_E164}">{C.PHONE_DISPLAY}</a><br>
          <a href="mailto:{C.EMAIL}">{C.EMAIL}</a><br>
          {C.HOURS_TEXT}
        </address>
      </div>
    </div>
    <div class="foot-base">
      <span>© <span data-year>{date.today().year}</span> {C.NAME}. All rights reserved.</span>
      <span>Interior designers in Ahmedabad, Gujarat</span>
    </div>
  </div>
</footer>
<a class="wa" href="https://wa.me/{C.WHATSAPP}?text={esc('Hello Shree Ohm Creation, I would like to discuss an interior project.')}" target="_blank" rel="noopener" aria-label="Chat on WhatsApp">{CHAT_ICON}<span>WhatsApp</span></a>'''


def page(path, title, desc, body, *, current=None, hero=False, schema=(), og_image=None, og_type="website", priority="0.7", robots="index,follow"):
    canonical = abs_url(path)
    og_img = og_image or abs_url("assets/img/og-default.jpg")
    ld = "\n".join(f'<script type="application/ld+json">{json.dumps(s, ensure_ascii=False)}</script>'
                   for s in [org_schema(), website_schema(), *schema])
    doc = f'''<!doctype html>
<html lang="en-IN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{canonical}">
<meta name="robots" content="{robots},max-image-preview:large">
<meta name="theme-color" content="#F5F3EF">
<meta name="geo.region" content="IN-{C.REGION_CODE}">
<meta name="geo.placename" content="{C.CITY}">
<meta name="geo.position" content="{C.LAT};{C.LNG}">
<meta name="ICBM" content="{C.LAT}, {C.LNG}">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="{C.NAME}">
<meta property="og:locale" content="en_IN">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{og_img}">
<meta property="og:image:alt" content="{C.NAME} Interiors">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(title)}">
<meta name="twitter:description" content="{esc(desc)}">
<meta name="twitter:image" content="{og_img}">
<link rel="icon" href="{u('assets/img/favicon.svg')}" type="image/svg+xml">
<link rel="icon" href="{u('assets/img/favicon-32.png')}" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="{u('assets/img/apple-touch-icon.png')}">
<link rel="manifest" href="{u('manifest.webmanifest')}">
<link rel="preconnect" href="https://images.unsplash.com">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;1,300;1,400&family=Montserrat:wght@400;500;600&display=swap">
<link rel="stylesheet" href="{u('assets/css/site.css')}?v={TODAY}">
{ld}
</head>
<body class="{'has-hero' if hero else ''}">
{header(current)}
<main id="main">
{body}
</main>
{footer()}
<script src="{u('assets/js/site.js')}?v={TODAY}" defer></script>
</body>
</html>
'''
    out = ROOT / path / "index.html" if not path.endswith(".html") else ROOT / path
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(doc)
    if robots.startswith("index"):
        PAGES.append((path, TODAY, priority))


def crumbs_html(trail):
    items = "".join(
        f'<li>{"<a href=" + chr(34) + u(p) + chr(34) + ">" + esc(n) + "</a>" if i < len(trail) - 1 else "<span aria-current=" + chr(34) + "page" + chr(34) + ">" + esc(n) + "</span>"}</li>'
        for i, (n, p) in enumerate(trail))
    return f'<nav aria-label="Breadcrumb"><ol class="crumbs">{items}</ol></nav>'


def pcard(p, sizes="(min-width: 760px) 50vw, 100vw"):
    return f'''<a class="pcard rv" href="{u('projects/' + p['slug'] + '/')}" data-cat="{p['cat']}">
  <div class="media">{img(p['hero'], p['name'] + ' — ' + p['type'] + ' interior in ' + p['location'], 1.25, sizes)}</div>
  <div class="meta"><h3>{esc(p['name'])}</h3><span>{esc(p['location'].split(',')[0])}</span></div>
  <p>{esc(p['type'])} · {esc(p['summary'])}</p>
</a>'''


def jcard(a):
    return f'''<a class="jcard rv" href="{u('journal/' + a['slug'] + '/')}">
  <div class="media">{img(a['img'], a['title'], 2/3, "(min-width: 760px) 33vw, 100vw", widths=(480, 800, 1200))}</div>
  <span class="label">{nice_date(a['date'])} · {a['read']}</span>
  <h3>{esc(a['title'])}</h3>
  <p>{esc(a['excerpt'])}</p>
</a>'''


def nice_date(iso):
    y, m, d = iso.split("-")
    months = "January February March April May June July August September October November December".split()
    return f"{int(d)} {months[int(m) - 1]} {y}"


def faq_html(faqs):
    return '<div class="faq">' + "".join(
        f'<details><summary>{esc(q)}</summary><div class="ans"><p>{esc(a)}</p></div></details>' for q, a in faqs) + "</div>"


def cta_band(title="Planning a new home?", text="Tell us about your space. The first site visit and consultation within Ahmedabad are free.", key="L11"):
    return f'''<section class="cta-band">
  {img(key, "", 0.5625, "100vw", widths=(800, 1400, 2200))}
  <div class="wrap">
    <span class="label" style="color:var(--on-dark-2)">Free consultation</span>
    <h2>{title}</h2>
    <p>{text}</p>
    <div class="hero-actions"><a class="btn light" href="{u('contact/')}">Book a site visit</a><a class="btn light" style="background:transparent;color:var(--on-dark)" href="https://wa.me/{C.WHATSAPP}" target="_blank" rel="noopener">WhatsApp us</a></div>
  </div>
</section>'''


def steps_html():
    return '<ol class="steps">' + "".join(
        f'<li><h3>{t}</h3><p>{d}</p><span class="time">{w}</span></li>' for t, d, w in PROCESS) + "</ol>"


def materials_html():
    return '<ul class="materials">' + "".join(f"<li><span>{a}</span><span>{b}</span></li>" for a, b in MATERIALS) + "</ul>"


# ---------------------------------------------------------------- pages
def build_home():
    feat = PROJECTS[0]
    svc_items = "".join(
        f'<li><a href="{u("services/" + s["slug"] + "/")}" data-img="{src(s["img"], 600, 1.25)}"><h3>{s["name"]}</h3><p>{esc(s["short"])}</p><span class="arr" aria-hidden="true">→</span></a></li>'
        for s in SERVICES)
    stats = "".join(f"<div><b>{n}</b><span>{l}</span></div>" for n, l in C.STATS)
    areas = "".join(f"<li>{a}</li>" for a in C.AREAS)
    body = f'''
<section class="hero">
  {img(feat['hero'], 'Living room of ' + feat['name'] + ', a bungalow interior by Shree Ohm Creation in Bopal, Ahmedabad', 0.625, "100vw", "cover", eager=True, widths=(800, 1200, 1600, 2200, 2800))}
  <div class="wrap">
    <h1><span class="kicker">Interior designers in Ahmedabad</span>Interiors, made to measure.</h1>
    <div class="hero-foot">
      <p>Modular kitchens, wardrobes, furniture and complete homes, designed in our studio and made in our own workshop in Kankaria.</p>
      <a class="link-line" href="{u('projects/' + feat['slug'] + '/')}">{feat['name']}, {feat['location'].split(',')[0]} <span aria-hidden="true">→</span></a>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap intro-grid">
    <p class="statement rv">For over a decade we have designed and built homes across Ahmedabad that are calm, practical and <em>made to last</em>.</p>
    <div class="side rv">
      <p>Shree Ohm Creation is an interior design studio with its own furniture workshop. We plan every room around the family who will live in it, then make the kitchen, wardrobes and furniture ourselves, so what you approve in 3D is what you get.</p>
      <a class="link-line" href="{u('studio/')}">About the studio <span aria-hidden="true">→</span></a>
    </div>
  </div>
</section>

<section class="section rule">
  <div class="wrap">
    <div class="sec-top"><div><span class="label">Selected work</span><h2>Recent projects across Ahmedabad</h2></div><a class="link-line" href="{u('projects/')}">All projects <span aria-hidden="true">→</span></a></div>
    <div class="pgrid editorial">{''.join(pcard(p) for p in PROJECTS[:4])}</div>
  </div>
</section>

<section class="section rule">
  <div class="wrap">
    <div class="sec-top"><div><span class="label">What we do</span><h2>Design, make, install</h2></div><a class="link-line" href="{u('services/')}">All services <span aria-hidden="true">→</span></a></div>
    <ul class="svc-list" data-preview>{svc_items}</ul>
  </div>
</section>

<section class="section dark">
  <div class="wrap" style="display:grid;gap:48px">
    <div class="sec-top" style="margin:0"><div><span class="label">The studio in numbers</span><h2>Made in Ahmedabad, for Ahmedabad</h2></div></div>
    <div class="stats">{stats}</div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="sec-top"><div><span class="label">How we work</span><h2>From first visit to handover in about twelve weeks</h2></div></div>
    {steps_html()}
  </div>
</section>

<section class="section paper rule">
  <div class="wrap split">
    <div class="media rv">{img('K6', 'White and wood kitchen with natural light, made in the Shree Ohm Creation workshop', 1.25, "(min-width: 900px) 50vw, 100vw")}</div>
    <div class="copy rv">
      <span class="label">Materials</span>
      <h2>Honest materials, named and guaranteed</h2>
      <p>We tell you exactly what goes into your home, from the grade of plywood to the brand of hinge. Waterproof plywood in kitchens, solid teak where strength matters, and finishes that age well.</p>
      {materials_html()}
      <a class="link-line" href="{u('journal/plywood-guide-bwp-vs-mr/')}">Read our plywood guide <span aria-hidden="true">→</span></a>
    </div>
  </div>
</section>

<section class="section rule">
  <div class="wrap">
    <div class="sec-top"><div><span class="label">Journal</span><h2>Guides for planning your home</h2></div><a class="link-line" href="{u('journal/')}">All articles <span aria-hidden="true">→</span></a></div>
    <div class="jgrid">{''.join(jcard(a) for a in ARTICLES[:3])}</div>
  </div>
</section>

<section class="section rule">
  <div class="wrap two-col">
    <h2>Questions we're often asked</h2>
    {faq_html(HOME_FAQS)}
  </div>
</section>

<section class="section tight rule">
  <div class="wrap" style="display:grid;gap:24px">
    <span class="label">Areas we serve in Ahmedabad &amp; Gandhinagar</span>
    <ul class="areas">{areas}</ul>
  </div>
</section>

{cta_band()}
'''
    page("", "Interior Designer in Ahmedabad | Shree Ohm Creation",
         "Interior designer in Ahmedabad for modular kitchens, wardrobes, custom furniture and complete home and office interiors. Book a free site visit.",
         body, hero=True, schema=[faq_schema(HOME_FAQS)], priority="1.0")


def build_projects():
    filters = "".join(f'<button type="button" data-filter="{k}" aria-pressed="{"true" if k == "all" else "false"}">{v}</button>' for k, v in PROJECT_CATS)
    body = f'''
<section class="page-head">
  <div class="wrap">
    {crumbs_html([("Home", ""), ("Projects", "projects/")])}
    <h1>Projects</h1>
    <p class="lead">Homes, kitchens, wardrobes and offices we have designed and built across Ahmedabad.</p>
  </div>
</section>
<section class="section tight" style="padding-top:0">
  <div class="wrap">
    <div class="filters" role="group" aria-label="Filter projects">{filters}</div>
    <div class="pgrid three">{''.join(pcard(p, "(min-width: 760px) 33vw, 100vw") for p in PROJECTS)}</div>
  </div>
</section>
{cta_band("Your home could be next.")}
'''
    items = {"@context": "https://schema.org", "@type": "ItemList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "url": abs_url(f"projects/{p['slug']}/"), "name": p["name"]} for i, p in enumerate(PROJECTS)]}
    page("projects/", "Interior Design Projects in Ahmedabad | SOC Interiors",
         "See homes, modular kitchens, wardrobes and offices designed and built by Shree Ohm Creation across Ahmedabad: Bopal, Satellite, Shela, Maninagar and more.",
         body, current="projects/", schema=[crumbs_schema([("Home", ""), ("Projects", "projects/")]), items], priority="0.9")

    for i, p in enumerate(PROJECTS):
        nxt = PROJECTS[(i + 1) % len(PROJECTS)]
        path = f"projects/{p['slug']}/"
        trail = [("Home", ""), ("Projects", "projects/"), (p["name"], path)]
        g = p["gallery"]
        gallery = (f'<figure class="wide rv">{img(g[0], p["name"] + " interior view", 0.5625, "100vw")}</figure>'
                   f'<figure class="rv">{img(g[1], p["name"] + " detail", 1.25, "50vw")}</figure>'
                   f'<figure class="rv">{img(g[2], p["name"] + " room view", 1.25, "50vw")}</figure>'
                   f'<figure class="wide rv">{img(g[3], p["name"] + " finished space", 0.5625, "100vw")}</figure>')
        facts = "".join(f"<div><dt>{k}</dt><dd>{esc(v)}</dd></div>" for k, v in
                        [("Location", p["location"]), ("Type", p["type"]), ("Size", p["area"]), ("Completed", p["year"]), ("Scope", p["scope"])])
        mats = "".join(f"<li><span>{a}</span><span>{b}</span></li>" for a, b in p["materials"])
        story = "".join(f"<p>{esc(s)}</p>" for s in p["story"])
        body = f'''
<section class="hero short">
  {img(p['hero'], p['name'] + ' — ' + p['type'] + ' interior design in ' + p['location'], 0.625, "100vw", "cover", eager=True, widths=(800, 1200, 1600, 2200))}
  <div class="wrap">
    {crumbs_html(trail)}
    <h1>{esc(p['name'])}</h1>
    <div class="hero-foot"><p>{esc(p['summary'])}</p><span class="label">{esc(p['type'])} · {esc(p['location'])}</span></div>
  </div>
</section>
<section class="section tight"><div class="wrap"><dl class="facts">{facts}</dl></div></section>
<section class="section tight" style="padding-top:0">
  <div class="wrap story">
    <h2>{esc(p['type'])} in {esc(p['location'].split(',')[0])}</h2>
    <div class="body">{story}</div>
  </div>
</section>
<section class="section tight" style="padding-top:0"><div class="wrap gallery">{gallery}</div></section>
<section class="section tight">
  <div class="wrap two-col">
    <h2>Materials</h2>
    <ul class="materials">{mats}</ul>
  </div>
</section>
<section class="section rule">
  <div class="wrap next-proj">
    <a class="media" href="{u('projects/' + nxt['slug'] + '/')}">{img(nxt['hero'], nxt['name'], 0.625, "(min-width: 900px) 50vw, 100vw")}</a>
    <div style="display:grid;gap:16px;justify-items:start">
      <span class="label">Next project</span>
      <a href="{u('projects/' + nxt['slug'] + '/')}" class="display h-xl">{esc(nxt['name'])}</a>
      <p class="muted" style="margin:0">{esc(nxt['type'])} · {esc(nxt['location'])}</p>
      <a class="link-line" href="{u('projects/')}">All projects <span aria-hidden="true">→</span></a>
    </div>
  </div>
</section>
{cta_band("Like what you see?", "Tell us about your home and we'll visit, measure and share ideas, free within Ahmedabad.")}
'''
        cw = {"@context": "https://schema.org", "@type": "CreativeWork", "name": p["name"], "about": p["type"],
              "description": p["summary"], "image": src(p["hero"], 1200, 0.625), "dateCreated": p["year"],
              "locationCreated": {"@type": "Place", "name": p["location"]}, "creator": {"@id": abs_url("#business")}}
        page(path, f"{p['name']}, {p['location'].split(',')[0]} | SOC Interiors",
             f"{p['summary']} {p['type']} by SOC Interiors, Ahmedabad.",
             body, current="projects/", hero=True, schema=[crumbs_schema(trail), cw],
             og_image=src(p["hero"], 1200, 0.525), priority="0.7")


def build_services():
    rows = "".join(
        f'<li><a href="{u("services/" + s["slug"] + "/")}" data-img="{src(s["img"], 600, 1.25)}"><h3>{s["name"]}</h3><p>{esc(s["short"])}</p><span class="arr" aria-hidden="true">→</span></a></li>'
        for s in SERVICES)
    body = f'''
<section class="page-head">
  <div class="wrap">
    {crumbs_html([("Home", ""), ("Services", "services/")])}
    <h1>Interior design services in Ahmedabad</h1>
    <p class="lead">One team for design, manufacturing and installation. Choose a single kitchen or wardrobe, or hand us the whole home.</p>
  </div>
</section>
<section class="section tight" style="padding-top:0"><div class="wrap"><ul class="svc-list" data-preview>{rows}</ul></div></section>
<section class="section rule"><div class="wrap"><div class="sec-top"><div><span class="label">Process</span><h2>How every project runs</h2></div></div>{steps_html()}</div></section>
{cta_band()}
'''
    page("services/", "Interior Design Services in Ahmedabad | SOC Interiors",
         "Home interiors, modular kitchens, wardrobes, custom furniture, offices and renovation in Ahmedabad. Designed, made and installed by one team.",
         body, current="services/", schema=[crumbs_schema([("Home", ""), ("Services", "services/")])], priority="0.9")

    for s in SERVICES:
        path = f"services/{s['slug']}/"
        trail = [("Home", ""), ("Services", "services/"), (s["name"], path)]
        incl = "".join(f"<li>{esc(x)}</li>" for x in s["includes"])
        rel = [p for p in PROJECTS if p["slug"] in s["projects"]][:3]
        others = "".join(f'<li><a href="{u("services/" + o["slug"] + "/")}" data-img="{src(o["img"], 600, 1.25)}"><h3>{o["name"]}</h3><p>{esc(o["short"])}</p><span class="arr" aria-hidden="true">→</span></a></li>'
                         for o in SERVICES if o is not s)
        body = f'''
<section class="hero short">
  {img(s['img'], s['h1'] + ' by Shree Ohm Creation', 0.625, "100vw", "cover", eager=True, widths=(800, 1200, 1600, 2200))}
  <div class="wrap">
    {crumbs_html(trail)}
    <h1>{esc(s['h1'])}</h1>
    <div class="hero-foot"><p>{esc(s['short'])}</p><a class="link-line" href="{u('contact/')}">Book a free site visit <span aria-hidden="true">→</span></a></div>
  </div>
</section>
<section class="section">
  <div class="wrap intro-grid">
    <p class="statement rv" style="font-size:var(--fs-lg);line-height:1.3">{esc(s['intro'])}</p>
    <div class="side rv"><p class="price-note">{esc(s['price'])}</p><a class="btn" href="{u('contact/')}">Get an estimate</a></div>
  </div>
</section>
<section class="section tight rule"><div class="wrap two-col"><h2>What's included</h2><ul class="incl">{incl}</ul></div></section>
<section class="section rule"><div class="wrap"><div class="sec-top"><div><span class="label">Process</span><h2>How it works</h2></div></div>{steps_html()}</div></section>
<section class="section rule"><div class="wrap"><div class="sec-top"><div><span class="label">Related work</span><h2>Projects</h2></div><a class="link-line" href="{u('projects/')}">All projects <span aria-hidden="true">→</span></a></div><div class="pgrid three">{''.join(pcard(p, "(min-width: 760px) 33vw, 100vw") for p in rel)}</div></div></section>
<section class="section rule"><div class="wrap two-col"><h2>Questions</h2>{faq_html(s['faqs'])}</div></section>
<section class="section tight rule"><div class="wrap"><div class="sec-top"><div><span class="label">More services</span></div></div><ul class="svc-list" data-preview>{others}</ul></div></section>
{cta_band()}
'''
        svc = {"@context": "https://schema.org", "@type": "Service", "name": s["name"], "serviceType": s["h1"],
               "description": s["intro"], "provider": {"@id": abs_url("#business")},
               "areaServed": [{"@type": "City", "name": "Ahmedabad"}, {"@type": "City", "name": "Gandhinagar"}],
               "url": abs_url(path), "image": src(s["img"], 1200, 0.625)}
        page(path, s["title"], s["desc"], body, current="services/", hero=True,
             schema=[crumbs_schema(trail), svc, faq_schema(s["faqs"])], og_image=src(s["img"], 1200, 0.525), priority="0.9")


def build_studio():
    trail = [("Home", ""), ("Studio", "studio/")]
    team = [("Founder", "Founder & principal designer"), ("Design", "Interior designers & 3D team"), ("Workshop", "Master carpenters & finishers"), ("Site", "Project managers & installers")]
    team_html = "".join(f'<figure><div class="ph">{n[0]}</div><figcaption><b>{n}</b><span>{r}</span></figcaption></figure>' for n, r in team)
    body = f'''
<section class="page-head">
  <div class="wrap">
    {crumbs_html(trail)}
    <h1>A design studio with its own workshop</h1>
    <p class="lead">Shree Ohm Creation started in Ahmedabad, making furniture by hand. Today we design and build complete homes and offices, still with our own carpenters.</p>
  </div>
</section>
<section class="section tight" style="padding-top:0"><div class="wrap">{img('L0', 'Calm, minimal interior with natural light', 0.5, "100vw", widths=(800, 1400, 2200))}</div></section>
<section class="section">
  <div class="wrap story">
    <h2>Our story</h2>
    <div class="body">
      <p>We began in {C.FOUNDED} as a small furniture workshop in Kankaria, making wardrobes, beds and modular kitchens for families across the east of the city. Word spread, and clients began asking us to design the whole home around the furniture.</p>
      <p>That is still how we work. Every project is designed in our studio and made in our own workshop, so the person who drew your kitchen can walk across and check it being built. It keeps quality high, timelines honest and prices fair.</p>
    </div>
  </div>
</section>
<section class="section rule">
  <div class="wrap">
    <div class="sec-top"><div><span class="label">What we believe</span><h2>Three things we won't compromise on</h2></div></div>
    <div class="values">
      <article><h3>Made to measure</h3><p>Every kitchen, wardrobe and bed is drawn and built for one room. Nothing comes from a catalogue.</p></article>
      <article><h3>Honest materials</h3><p>We name the plywood, veneer and hardware in every quote, and show you the sheets before we cut them.</p></article>
      <article><h3>Calm design</h3><p>Clean lines and warm, natural tones that still feel right ten years later.</p></article>
    </div>
  </div>
</section>
<section class="section dark">
  <div class="wrap split flip">
    <div class="media rv">{img('D0', 'Dining area with warm wood and soft pendant lights', 1.25, "(min-width: 900px) 50vw, 100vw")}</div>
    <div class="copy rv">
      <span class="label">The workshop</span>
      <h2>Built by our own hands in Kankaria</h2>
      <p>Our workshop has panel saws, edge-banding and spray booths for PU and lacquer, run by carpenters who have been with us for years. Making in-house means we control every joint, every edge and every finish.</p>
      {materials_html()}
    </div>
  </div>
</section>
<section class="section"><div class="wrap"><div class="sec-top"><div><span class="label">Process</span><h2>How we work</h2></div></div>{steps_html()}</div></section>
<section class="section rule">
  <div class="wrap">
    <div class="sec-top"><div><span class="label">The team</span><h2>Designers, makers and site managers</h2></div></div>
    <div class="team">{team_html}</div>
  </div>
</section>
{cta_band("Come and see the workshop.", "Visit us in Kankaria to see materials, finishes and furniture being made.")}
'''
    about = {"@context": "https://schema.org", "@type": "AboutPage", "name": "About Shree Ohm Creation", "url": abs_url("studio/"), "about": {"@id": abs_url("#business")}}
    page("studio/", "About Us | Interior Studio & Workshop, Ahmedabad | SOC",
         "Shree Ohm Creation is an Ahmedabad interior design studio with its own furniture workshop in Kankaria. Meet the team and see how we design, make and install.",
         body, current="studio/", schema=[crumbs_schema(trail), about], priority="0.8")


def build_journal():
    trail = [("Home", ""), ("Journal", "journal/")]
    body = f'''
<section class="page-head">
  <div class="wrap">
    {crumbs_html(trail)}
    <h1>Journal</h1>
    <p class="lead">Practical guides on costs, materials and design for homes in Ahmedabad.</p>
  </div>
</section>
<section class="section tight" style="padding-top:0"><div class="wrap"><div class="jgrid">{''.join(jcard(a) for a in ARTICLES)}</div></div></section>
{cta_band()}
'''
    blog = {"@context": "https://schema.org", "@type": "Blog", "name": f"{C.NAME} Journal", "url": abs_url("journal/"),
            "blogPost": [{"@type": "BlogPosting", "headline": a["title"], "url": abs_url(f"journal/{a['slug']}/"), "datePublished": a["date"]} for a in ARTICLES]}
    page("journal/", "Interior Design Guides for Ahmedabad Homes | SOC Journal",
         "Practical guides on modular kitchen costs, plywood, wardrobes and 3BHK interiors in Ahmedabad, written by the Shree Ohm Creation team.",
         body, current="journal/", schema=[crumbs_schema(trail), blog], priority="0.8")

    for a in ARTICLES:
        path = f"journal/{a['slug']}/"
        trail = [("Home", ""), ("Journal", "journal/"), (a["title"], path)]
        more = [x for x in ARTICLES if x is not a][:3]
        body = f'''
<article>
  <section class="page-head" style="padding-bottom:32px">
    <div class="wrap article" style="display:grid;gap:20px">
      {crumbs_html(trail)}
      <h1 style="font-size:var(--fs-xl);max-width:none">{esc(a['title'])}</h1>
      <div class="article-meta"><span>{nice_date(a['date'])}</span><span>{a['read']}</span><span>By the {C.NAME} team</span></div>
    </div>
  </section>
  <div class="wrap article-hero" style="max-width:1100px">{img(a['img'], a['title'], 0.5625, "(min-width: 1100px) 1100px, 100vw", eager=True)}</div>
  <section class="section tight">
    <div class="wrap"><div class="article"><div class="body">{a['body'].replace('{base}', C.BASE)}</div></div></div>
  </section>
</article>
<section class="section rule"><div class="wrap"><div class="sec-top"><div><span class="label">Keep reading</span><h2>More guides</h2></div></div><div class="jgrid">{''.join(jcard(x) for x in more)}</div></div></section>
{cta_band()}
'''
        art = {"@context": "https://schema.org", "@type": "BlogPosting", "headline": a["title"], "description": a["desc"],
               "image": src(a["img"], 1200, 0.5625), "datePublished": a["date"], "dateModified": a["date"],
               "author": {"@type": "Organization", "name": C.NAME, "url": abs_url()},
               "publisher": {"@id": abs_url("#business")}, "mainEntityOfPage": abs_url(path), "inLanguage": "en-IN"}
        page(path, a["seo_title"], a["desc"], body, current="journal/", schema=[crumbs_schema(trail), art],
             og_image=src(a["img"], 1200, 0.525), og_type="article", priority="0.7")


def build_contact():
    trail = [("Home", ""), ("Contact", "contact/")]
    types = ["Complete home interior", "Modular kitchen", "Wardrobes", "Custom furniture", "Office or commercial", "Renovation", "Something else"]
    opts = "".join(f"<option>{t}</option>" for t in types)
    budgets = ["Under ₹3 lakh", "₹3 – 8 lakh", "₹8 – 15 lakh", "₹15 – 25 lakh", "Above ₹25 lakh", "Not sure yet"]
    bopts = '<option value="">Select</option>' + "".join(f"<option>{b}</option>" for b in budgets)
    body = f'''
<section class="page-head">
  <div class="wrap">
    {crumbs_html(trail)}
    <h1>Let's talk about your space</h1>
    <p class="lead">Tell us a little about your project. We reply within one working day, and the first site visit within Ahmedabad is free.</p>
  </div>
</section>
<section class="section tight" style="padding-top:0">
  <div class="wrap contact-grid">
    <div class="contact-info">
      <div class="item"><span class="label">Call or WhatsApp</span><a class="big" href="tel:{C.PHONE_E164}">{C.PHONE_DISPLAY}</a></div>
      <div class="item"><span class="label">Email</span><a class="big" href="mailto:{C.EMAIL}">{C.EMAIL}</a></div>
      <div class="item"><span class="label">Studio &amp; workshop</span><address style="font-style:normal">{C.STREET}<br>{C.LOCALITY}, {C.CITY}, {C.REGION} {C.POSTCODE}</address><a class="link-line" href="{C.MAPS_URL}" target="_blank" rel="noopener">Open in Google Maps <span aria-hidden="true">→</span></a></div>
      <div class="item"><span class="label">Hours</span><p>{C.HOURS_TEXT}. Site visits by appointment.</p></div>
    </div>
    <form class="form" id="enquiry" data-wa="{C.WHATSAPP}" novalidate>
      <div class="field"><label for="f-name">Your name</label><input id="f-name" name="name" autocomplete="name" required></div>
      <div class="field"><label for="f-phone">Phone</label><input id="f-phone" name="phone" type="tel" autocomplete="tel" inputmode="tel" required></div>
      <div class="field"><label for="f-area">Area in Ahmedabad</label><input id="f-area" name="area" placeholder="e.g. Satellite"></div>
      <div class="field"><label for="f-type">Project</label><select id="f-type" name="type" required>{opts}</select></div>
      <div class="field full"><label for="f-budget">Approximate budget</label><select id="f-budget" name="budget">{bopts}</select></div>
      <div class="field full"><label for="f-msg">Tell us about your space</label><textarea id="f-msg" name="message" placeholder="Flat size, possession date, rooms you want done…"></textarea></div>
      <div class="full" style="display:grid;gap:12px;justify-items:start">
        <button class="btn" type="submit">Send via WhatsApp</button>
        <p class="note">Your details open in WhatsApp so you can send them straight to us. Nothing is stored on this website.</p>
        <p class="form-status" role="status" aria-live="polite"></p>
      </div>
    </form>
  </div>
</section>
<section class="section tight rule">
  <div class="wrap"><iframe class="map" title="Map showing {C.NAME} in {C.LOCALITY}, {C.CITY}" loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="https://maps.google.com/maps?q={C.LAT},{C.LNG}&z=14&output=embed"></iframe></div>
</section>
<section class="section rule"><div class="wrap two-col"><h2>Before you get in touch</h2>{faq_html(HOME_FAQS[:4])}</div></section>
'''
    contact = {"@context": "https://schema.org", "@type": "ContactPage", "name": "Contact Shree Ohm Creation", "url": abs_url("contact/"), "about": {"@id": abs_url("#business")}}
    page("contact/", "Contact | Free Interior Consultation in Ahmedabad | SOC",
         f"Call {C.PHONE_DISPLAY} or WhatsApp Shree Ohm Creation to book a free site visit for your home, kitchen or office interior in Ahmedabad. Studio in Kankaria.",
         body, current="contact/", schema=[crumbs_schema(trail), contact], priority="0.9")


def build_404():
    body = f'''<section class="nf"><div class="wrap"><span class="label">Page not found</span><h1 class="display h-xl">This room doesn't exist.</h1><p class="muted">The page may have moved. Try one of these instead.</p><div class="hero-actions"><a class="btn" href="{u()}">Home</a><a class="btn ghost" href="{u('projects/')}">Projects</a><a class="btn ghost" href="{u('contact/')}">Contact</a></div></div></section>'''
    page("404.html", "Page not found | Shree Ohm Creation", "This page could not be found.", body, robots="noindex,follow")


def build_meta_files():
    urls = "\n".join(f"  <url><loc>{abs_url(p)}</loc><lastmod>{m}</lastmod><priority>{pr}</priority></url>" for p, m, pr in PAGES)
    (ROOT / "sitemap.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}\n</urlset>\n')
    (ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {abs_url('sitemap.xml')}\n")
    (ROOT / "manifest.webmanifest").write_text(json.dumps({
        "name": C.NAME, "short_name": "SOC Interiors", "start_url": C.BASE, "scope": C.BASE, "display": "standalone",
        "background_color": "#F5F3EF", "theme_color": "#F5F3EF",
        "icons": [{"src": u("assets/img/icon-192.png"), "sizes": "192x192", "type": "image/png"},
                  {"src": u("assets/img/icon-512.png"), "sizes": "512x512", "type": "image/png"}]}, indent=2))
    (ROOT / ".nojekyll").write_text("")


if __name__ == "__main__":
    build_home()
    build_projects()
    build_services()
    build_studio()
    build_journal()
    build_contact()
    build_404()
    build_meta_files()
    print(f"Built {len(PAGES)} indexable pages + 404 into {ROOT}")
