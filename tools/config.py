"""Business details used across the whole site.

Anything marked DUMMY is a placeholder. Replace it with the real value, then run:
    python3 tools/build.py
"""

SITE_URL = "https://nisarg2810.github.io/soc/"   # change if you move to a custom domain
BASE = "/soc/"                                    # path the site is served from ("/" on a custom domain)

NAME = "Shree Ohm Creation"
SHORT = "SOC Interiors"
TAGLINE = "Interior designers and bespoke furniture makers in Ahmedabad"

PHONE_DISPLAY = "+91 90000 00000"        # DUMMY
PHONE_E164 = "+919000000000"             # DUMMY
WHATSAPP = "919000000000"                # DUMMY (country code + number, no +)
EMAIL = "hello@shreeohmcreation.in"      # DUMMY

STREET = "Plot 00, Vatva GIDC Phase 1"   # DUMMY street line
LOCALITY = "Vatva"
CITY = "Ahmedabad"
REGION = "Gujarat"
REGION_CODE = "GJ"
POSTCODE = "382440"
COUNTRY = "IN"
LAT, LNG = 22.9707, 72.6325              # approximate, Vatva. Set to the exact studio pin.
MAPS_URL = "https://www.google.com/maps/search/?api=1&query=Shree+Ohm+Creation+Vatva+Ahmedabad"

HOURS_TEXT = "Monday to Saturday, 10 am to 7 pm"   # DUMMY
HOURS_SCHEMA = [{"days": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"], "opens": "10:00", "closes": "19:00"}]

FOUNDED = "2014"                         # from the IndiaMART listing (12 years). Confirm.

# DUMMY figures shown on the home page. Replace with real numbers.
STATS = [
    ("12+", "Years in Ahmedabad"),
    ("350+", "Homes completed"),
    ("1,200+", "Kitchens and wardrobes"),
    ("35", "Carpenters and finishers"),
]

# Add real profile links when they exist, e.g. "https://www.instagram.com/yourhandle/"
SOCIAL = {
    "Instagram": "",
    "Facebook": "",
    "Pinterest": "",
    "YouTube": "",
}

AREAS = [
    "Vatva", "Maninagar", "Isanpur", "Narol", "Ghodasar", "Naroda", "Nikol", "Bapunagar",
    "Satellite", "Bopal", "South Bopal", "Shela", "Prahlad Nagar", "Vastrapur", "Thaltej",
    "Bodakdev", "SG Highway", "Navrangpura", "Paldi", "Gota", "Chandkheda", "Gandhinagar",
]
