# Placeholders to replace before promoting the site

The site was built with placeholder content wherever real details were not available.
Replace these before sharing the link widely or running ads.

## Must replace (customers will act on these)

| What | Where | Current placeholder |
|---|---|---|
| Phone number | `tools/config.py` → `PHONE_DISPLAY`, `PHONE_E164` | +91 90000 00000 |
| WhatsApp number | `tools/config.py` → `WHATSAPP` | 919000000000 |
| Email | `tools/config.py` → `EMAIL` | hello@shreeohmcreation.in |
| Street address | `tools/config.py` → `STREET` | Plot 00, Vatva GIDC Phase 1 |
| Map pin | `tools/config.py` → `LAT`, `LNG` | approximate Vatva location |
| Opening hours | `tools/config.py` → `HOURS_TEXT`, `HOURS_SCHEMA` | Mon–Sat, 10 am–7 pm |

## Must replace (honesty)

| What | Where | Note |
|---|---|---|
| All project photos | `tools/content.py` → `PROJECTS` (`hero`, `gallery`) | Free Unsplash stock photos, not Shree Ohm Creation's work. Replace with real project photos. |
| Project names, locations, sizes, stories | `tools/content.py` → `PROJECTS` | Invented examples. Replace with real projects. |
| Studio numbers (350+ homes etc.) | `tools/config.py` → `STATS` | Invented. Use real figures or remove. |
| Founding year | `tools/config.py` → `FOUNDED` | 2014, based on "12 years" on IndiaMART. Confirm. |
| Team section | `tools/build.py` → `build_studio()` | Generic roles. Add real names and photos. |

## Good to review

| What | Where |
|---|---|
| Price ranges on service pages and in articles | `tools/content.py` → `SERVICES[*].price`, `ARTICLES` |
| Social profile links (hidden until filled) | `tools/config.py` → `SOCIAL` |
| Service photos, journal photos, studio photos | `tools/content.py`, `tools/build.py` (Unsplash stock) |

## How to use your own photos

1. Put photos in `assets/img/projects/` (JPG or WebP, about 2000 px wide, under 400 KB each).
2. Change the `img()` helper in `tools/build.py` to point at local files, or ask Claude to wire it up.
3. Run `python3 tools/build.py`, commit and push.
