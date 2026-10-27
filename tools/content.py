"""Site content. Projects and their photos are DUMMY placeholders (Unsplash stock)
until real project photography is added. Image keys refer to tools/img_idx.json."""

# ---------------------------------------------------------------- projects
PROJECTS = [
    {
        "slug": "the-teak-house-bopal",
        "name": "The Teak House",
        "location": "Bopal, Ahmedabad",
        "type": "4BHK bungalow",
        "cat": "residential",
        "area": "4,200 sq ft",
        "year": "2025",
        "scope": "Full interiors, furniture, lighting",
        "hero": "L5",
        "gallery": ["L4", "D7", "B1", "K3"],
        "summary": "A bungalow opened up to its garden, with teak, lime plaster and very little else.",
        "story": [
            "The family wanted a house that felt calm the moment you walked in, with space for three generations and a garden you could see from every room.",
            "We took down two internal walls to join the living and dining areas, then kept the palette to teak, warm white plaster and natural stone. All storage is built in and flush, so the rooms stay clear. The kitchen, wardrobes, beds and dining table were all made in our Vatva workshop.",
        ],
        "materials": [("Joinery", "Teak veneer on BWP plywood"), ("Walls", "Lime plaster finish"), ("Kitchen", "Matte PU shutters, quartz top"), ("Hardware", "Hettich soft-close")],
    },
    {
        "slug": "satellite-residence",
        "name": "Satellite Residence",
        "location": "Satellite, Ahmedabad",
        "type": "3BHK apartment",
        "cat": "residential",
        "area": "1,850 sq ft",
        "year": "2025",
        "scope": "Full interiors, modular kitchen, wardrobes",
        "hero": "L2",
        "gallery": ["L7", "D8", "B0", "W5"],
        "summary": "A soft grey apartment for a young family, with storage hidden in every wall.",
        "story": [
            "A young couple with one child wanted their first home to feel larger than its 1,850 sq ft, and they did not want clutter on show.",
            "We planned full-height storage along one wall of each room and finished it in the same tone as the walls, so it almost disappears. The living room has a low walnut TV unit, a reading corner by the window and lighting on three separate circuits for day, evening and night.",
        ],
        "materials": [("Wardrobes", "Laminate on BWP plywood, sliding"), ("TV unit", "Walnut veneer"), ("Kitchen", "Acrylic gloss, L-shaped"), ("Lighting", "Profile LED, warm 3000K")],
    },
    {
        "slug": "walnut-and-white-kitchen-prahlad-nagar",
        "name": "Walnut & White Kitchen",
        "location": "Prahlad Nagar, Ahmedabad",
        "type": "Modular kitchen",
        "cat": "kitchens",
        "area": "180 sq ft",
        "year": "2024",
        "scope": "Kitchen design, manufacture and installation",
        "hero": "K0",
        "gallery": ["K5", "K8", "K10", "K7"],
        "summary": "An island kitchen in walnut veneer and white, built for a family that cooks every day.",
        "story": [
            "The brief was simple: a kitchen that can take daily Gujarati cooking for six people and still look good when guests walk through.",
            "We used walnut veneer for tall units, white matte shutters for the base run and a quartz top that handles heat and turmeric. Every drawer was planned around what goes inside it: thalis, masala dabbas, pressure cookers and steel dabbas each have a place.",
        ],
        "materials": [("Tall units", "Walnut veneer, PU lacquer"), ("Base units", "White matte laminate"), ("Counter", "Quartz, 20 mm"), ("Hardware", "Hettich tandem drawers")],
    },
    {
        "slug": "maninagar-family-home",
        "name": "Maninagar Family Home",
        "location": "Maninagar, Ahmedabad",
        "type": "3BHK renovation",
        "cat": "residential renovation",
        "area": "1,600 sq ft",
        "year": "2024",
        "scope": "Renovation, furniture, kitchen",
        "hero": "L15",
        "gallery": ["D1", "B5", "D2", "L9"],
        "summary": "A 20-year-old flat renovated while keeping the family's favourite pieces.",
        "story": [
            "This family had lived in the flat for twenty years and loved it, but the kitchen was tired and storage had run out.",
            "We reworked the plan room by room, kept the original teak dining table and a carved temple unit, and built new pieces around them. The renovation was phased so the family could stay at home through most of the work.",
        ],
        "materials": [("Shelving", "Oak veneer, open and closed"), ("Dining", "Restored teak table"), ("Flooring", "Vitrified wood-look tiles"), ("Kitchen", "Laminate, parallel layout")],
    },
    {
        "slug": "sg-highway-studio-office",
        "name": "SG Highway Studio Office",
        "location": "SG Highway, Ahmedabad",
        "type": "Office interior",
        "cat": "commercial",
        "area": "3,000 sq ft",
        "year": "2024",
        "scope": "Office planning, furniture, cabins",
        "hero": "O2",
        "gallery": ["O1", "O3", "O6", "O7"],
        "summary": "A bright workplace for a 30-person team, with glass cabins and a long shared table.",
        "story": [
            "A growing consultancy needed an office that felt open but still gave its partners quiet rooms for calls.",
            "We placed glass cabins along the inner wall so daylight reaches the whole floor, and built a single long work table in oak for the team. Acoustic panels are hidden behind slatted wood, and every desk has power and data built into it.",
        ],
        "materials": [("Work tables", "Oak veneer, custom length"), ("Cabins", "Toughened glass, aluminium frame"), ("Acoustics", "Slatted wood over felt"), ("Storage", "Laminate, lockable")],
    },
    {
        "slug": "shela-penthouse",
        "name": "Shela Penthouse",
        "location": "Shela, Ahmedabad",
        "type": "Wardrobes & bedrooms",
        "cat": "wardrobes residential",
        "area": "4 bedrooms",
        "year": "2025",
        "scope": "Wardrobes, walk-in closet, beds",
        "hero": "W3",
        "gallery": ["W0", "W2", "W4", "B2"],
        "summary": "Four bedrooms and a walk-in closet, each wardrobe planned to the shelf.",
        "story": [
            "The owners asked for wardrobes that looked like furniture, not boxes, and a walk-in closet for the main bedroom.",
            "We measured each person's clothes, shoes and bags before drawing a single shelf. The walk-in has open hanging, glass-front drawers and a dressing mirror with soft lighting. Children's rooms got lower rails that can be raised as they grow.",
        ],
        "materials": [("Shutters", "Fluted veneer, lacquered"), ("Interiors", "Light oak laminate"), ("Lighting", "Sensor LED strips"), ("Hardware", "Hettich hinges and lifts")],
    },
]

PROJECT_CATS = [("all", "All"), ("residential", "Homes"), ("kitchens", "Kitchens"), ("wardrobes", "Wardrobes"), ("commercial", "Offices"), ("renovation", "Renovation")]

# ---------------------------------------------------------------- services
SERVICES = [
    {
        "slug": "residential-interior-design",
        "name": "Residential Interiors",
        "h1": "Home interior design in Ahmedabad",
        "title": "Home Interior Designer in Ahmedabad | Shree Ohm Creation",
        "desc": "Complete home interiors in Ahmedabad for flats, bungalows and villas. Design, 3D views, furniture and installation by one team. Book a free consultation.",
        "img": "L1",
        "short": "Complete interiors for flats, bungalows and villas, from first sketch to handover.",
        "intro": "We design and build complete interiors for 2BHK, 3BHK and 4BHK flats, bungalows and villas across Ahmedabad. One team handles the layout, 3D views, furniture, false ceiling, lighting and installation, so you deal with one person from the first visit to the day you move in.",
        "includes": ["Site measurement and space planning", "Mood boards and photo-realistic 3D views", "Modular kitchen and wardrobes", "TV units, beds, study and pooja units", "False ceiling, lighting and electrical layout", "Paint, wallpaper and wall panelling", "Curtains, blinds and soft furnishing", "Site supervision and final handover"],
        "price": "Most complete 3BHK interiors in Ahmedabad fall between ₹8 lakh and ₹22 lakh, depending on size, materials and how much is built in. We share a line-by-line estimate after the first site visit.",
        "faqs": [
            ("How long does a full home interior take?", "A typical 3BHK takes 8 to 12 weeks from design sign-off. Furniture is made in our workshop while site work goes on, which saves time."),
            ("Do you work on new flats from builders?", "Yes. Most of our homes are new flats in Ahmedabad. We can start measuring as soon as you get possession and the flooring is done."),
            ("Can I see the design before work starts?", "Yes. You approve 2D layouts and 3D views of every room before anything is made."),
        ],
        "projects": ["the-teak-house-bopal", "satellite-residence", "maninagar-family-home"],
    },
    {
        "slug": "modular-kitchen-ahmedabad",
        "name": "Modular Kitchens",
        "h1": "Modular kitchens in Ahmedabad",
        "title": "Modular Kitchen in Ahmedabad | Made to Measure | SOC",
        "desc": "Modular kitchens made to measure in our Ahmedabad workshop. L-shaped, parallel, U-shaped and island kitchens in BWP plywood with Hettich fittings.",
        "img": "K2",
        "short": "L-shaped, parallel, U-shaped and island kitchens, made in our own workshop.",
        "intro": "Every kitchen we make is planned around how your family cooks. We measure the room, plan where the hob, sink and fridge go, and design drawers for your actual utensils. Carcasses are made from waterproof BWP plywood in our Vatva workshop and fitted with soft-close hardware.",
        "includes": ["Layout planning: straight, L, parallel, U or island", "BWP plywood carcasses, waterproof", "Laminate, acrylic, PU or veneer shutters", "Quartz or granite counters", "Tandem drawers, corner units and tall pantry", "Chimney, hob and appliance integration", "Under-cabinet lighting", "Installation and after-sales service"],
        "price": "An L-shaped modular kitchen in Ahmedabad usually costs between ₹1.8 lakh and ₹4 lakh. Finish, hardware and the number of tall units make the biggest difference.",
        "faqs": [
            ("Which material is best for a modular kitchen in Ahmedabad?", "We recommend BWP (boiling water proof) plywood for carcasses, especially under the sink. It handles water and humidity far better than MDF or particle board."),
            ("How long does a modular kitchen take?", "About 3 to 5 weeks from final design to installation. Fitting on site takes 3 to 5 days."),
            ("Do you give a warranty?", "Yes. Carcasses and workmanship carry our warranty, and hardware carries the manufacturer's warranty."),
        ],
        "projects": ["walnut-and-white-kitchen-prahlad-nagar", "satellite-residence", "the-teak-house-bopal"],
    },
    {
        "slug": "wardrobe-design-ahmedabad",
        "name": "Wardrobes & Storage",
        "h1": "Wardrobes and walk-in closets in Ahmedabad",
        "title": "Wardrobe Designer & Maker in Ahmedabad | SOC Interiors",
        "desc": "Sliding and hinged wardrobes, walk-in closets and storage made to measure in Ahmedabad. Laminate, veneer, glass and PU finishes with soft-close fittings.",
        "img": "W6",
        "short": "Sliding and hinged wardrobes, walk-in closets and storage, planned to the shelf.",
        "intro": "A good wardrobe starts with what goes inside it. We plan hanging, shelves and drawers around your clothes, then choose sliding or hinged doors to suit the room. Every wardrobe is made to measure, floor to ceiling, so no space is wasted.",
        "includes": ["Sliding, hinged and walk-in wardrobes", "Loft storage up to the ceiling", "Internal drawers, trouser racks and shoe pull-outs", "Mirror, glass and fluted shutters", "Sensor LED lighting", "Dressing units and study combinations", "Children's wardrobes that grow with them", "Soft-close hinges and channels"],
        "price": "Wardrobes in Ahmedabad typically cost ₹1,100 to ₹2,500 per sq ft of front area, depending on shutter finish and internal fittings.",
        "faqs": [
            ("Sliding or hinged: which is better?", "Sliding doors suit smaller rooms because they need no swing space. Hinged doors give full access and cost less. Read our guide for a full comparison."),
            ("Can you make a wardrobe in a rented flat?", "Yes. We can make free-standing wardrobes that can be taken apart and moved."),
        ],
        "projects": ["shela-penthouse", "satellite-residence", "the-teak-house-bopal"],
    },
    {
        "slug": "custom-furniture-ahmedabad",
        "name": "Bespoke Furniture",
        "h1": "Custom furniture made in Ahmedabad",
        "title": "Custom Furniture Maker in Ahmedabad | SOC Interiors",
        "desc": "Beds, sofas, dining tables, TV units and study desks made to order in our Ahmedabad workshop. Teak, veneer and PU finishes, built to your size.",
        "img": "L6",
        "short": "Beds, sofas, dining sets, TV units and study desks, made to order.",
        "intro": "Our furniture is made by our own carpenters in Vatva. You choose the size, wood and finish, and we build it for your room. Many clients start with one piece, such as a bed or a dining table, and come back for the rest of the house.",
        "includes": ["King and queen beds with storage", "Sofas and lounge chairs", "Dining tables and chairs", "TV and media units", "Study desks and bookshelves", "Pooja units", "Teak, veneer, laminate and PU finishes", "Upholstery in your choice of fabric"],
        "price": "A storage bed starts from about ₹45,000 and a six-seater dining set from about ₹60,000. Wood, size and upholstery change the price.",
        "faqs": [
            ("Can you copy a design I saw online?", "We can make a piece inspired by a photo, adjusted to your size and budget. We don't copy protected designs exactly."),
            ("Do you use solid wood?", "We use solid teak where it matters, such as table legs and frames, and veneered BWP plywood for large panels so they don't warp."),
        ],
        "projects": ["the-teak-house-bopal", "maninagar-family-home", "shela-penthouse"],
    },
    {
        "slug": "office-interior-design-ahmedabad",
        "name": "Office & Commercial",
        "h1": "Office interior design in Ahmedabad",
        "title": "Office Interior Designer in Ahmedabad | Shree Ohm Creation",
        "desc": "Office, clinic and showroom interiors in Ahmedabad. Space planning, cabins, workstations and custom furniture delivered on time and on budget.",
        "img": "O5",
        "short": "Offices, clinics and showrooms planned for the way your team works.",
        "intro": "We design and fit out offices, clinics, showrooms and small retail spaces across Ahmedabad. We plan the layout around your team, then build cabins, workstations, reception and storage in our workshop to keep site time short.",
        "includes": ["Space planning and seating layouts", "Reception and waiting areas", "Glass cabins and meeting rooms", "Custom workstations and storage", "False ceiling, lighting and acoustics", "Electrical, data and AC coordination", "Branding walls and signage", "Weekend and after-hours installation"],
        "price": "Office fit-outs in Ahmedabad usually range from ₹1,500 to ₹3,500 per sq ft, depending on cabins, ceiling and furniture.",
        "faqs": [
            ("Can you work while our office is running?", "Yes. We phase the work and can install furniture at night or on weekends."),
            ("Do you handle commercial showrooms?", "Yes. We design showrooms and retail counters as well as offices and clinics."),
        ],
        "projects": ["sg-highway-studio-office"],
    },
    {
        "slug": "home-renovation-ahmedabad",
        "name": "Renovation & Turnkey",
        "h1": "Home renovation in Ahmedabad",
        "title": "Home Renovation & Turnkey Interiors in Ahmedabad | SOC",
        "desc": "Renovate an older flat or bungalow in Ahmedabad with one team: civil work, electrical, plumbing, kitchen, wardrobes and finishing, handed over ready to live in.",
        "img": "L13",
        "short": "Older homes renovated room by room, handed over ready to live in.",
        "intro": "Renovation is harder than a new flat: walls are not straight, wiring is old and families often live at home during the work. We plan the work in phases, handle civil, electrical and plumbing changes, and finish with new furniture so the home is ready to live in.",
        "includes": ["Condition survey and renovation plan", "Civil changes, tiling and waterproofing", "New wiring and plumbing", "Kitchen and bathroom upgrades", "Wardrobes and furniture", "Painting and polishing", "Phased work so you can stay at home", "One point of contact throughout"],
        "price": "Renovation costs depend heavily on civil work. We visit, inspect and give a fixed estimate before starting.",
        "faqs": [
            ("Can we live at home during renovation?", "Usually yes. We work room by room and keep one bathroom and the kitchen running for as long as possible."),
            ("Do you keep existing furniture?", "If you love a piece, we restore it and design around it."),
        ],
        "projects": ["maninagar-family-home", "the-teak-house-bopal"],
    },
]

# ---------------------------------------------------------------- process
PROCESS = [
    ("Consultation", "We visit your site, measure every room and listen to how you live. Free within Ahmedabad.", "Week 1"),
    ("Design & 3D", "Layouts, materials and photo-realistic 3D views of each room, revised until they feel right.", "Weeks 2–4"),
    ("Making", "Furniture is made in our Vatva workshop while civil, electrical and ceiling work goes on at site.", "Weeks 4–10"),
    ("Installation", "Our own team fits, finishes and cleans. We walk you through every room at handover.", "Weeks 10–12"),
]

MATERIALS = [
    ("BWP plywood", "Waterproof, for kitchens and wardrobes"),
    ("Teak", "Solid wood for frames and legs"),
    ("Veneer", "Walnut, oak and teak, PU lacquered"),
    ("Laminates", "Matte, suede and high gloss"),
    ("PU & acrylic", "Seamless painted finishes"),
    ("Hardware", "Hettich soft-close fittings"),
]

HOME_FAQS = [
    ("How much does interior design cost in Ahmedabad?", "It depends on size and materials. As a guide, a complete 3BHK usually costs ₹8 lakh to ₹22 lakh, a modular kitchen ₹1.8 lakh to ₹4 lakh and wardrobes ₹1,100 to ₹2,500 per sq ft. We give a detailed estimate after a free site visit."),
    ("Do you make the furniture yourselves?", "Yes. Kitchens, wardrobes and furniture are made in our own workshop in Vatva, Ahmedabad, which lets us control quality and timelines."),
    ("Which areas of Ahmedabad do you cover?", "All of Ahmedabad and Gandhinagar, including Satellite, Bopal, Shela, Prahlad Nagar, Thaltej, Maninagar, Vatva, Naroda, Gota and Chandkheda."),
    ("Is the first consultation free?", "Yes. The first site visit and consultation within Ahmedabad are free."),
    ("How long does a complete home interior take?", "Most 3BHK homes take 8 to 12 weeks after the design is approved."),
]

# ---------------------------------------------------------------- journal
ARTICLES = [
    {
        "slug": "modular-kitchen-cost-ahmedabad",
        "title": "Modular kitchen cost in Ahmedabad: a 2026 price guide",
        "seo_title": "Modular Kitchen Cost in Ahmedabad (2026 Price Guide)",
        "desc": "What a modular kitchen costs in Ahmedabad in 2026, by layout and finish. Price ranges, what changes the cost, and how to plan your budget.",
        "img": "K4",
        "date": "2026-09-18",
        "read": "6 min read",
        "excerpt": "Price ranges by layout and finish, and the five things that change the cost most.",
        "body": """
<p>The most common question we hear is “how much will my kitchen cost?” The honest answer is that it depends on size, layout and finish. This guide gives you realistic 2026 price ranges for Ahmedabad so you can plan before you meet any designer.</p>
<div class="callout"><b>Quick answer</b>Most modular kitchens in Ahmedabad cost between ₹1.2 lakh and ₹6 lakh. A typical L-shaped kitchen in a 3BHK flat costs ₹1.8 lakh to ₹4 lakh with BWP plywood, laminate shutters and soft-close hardware.</div>
<h2>Price by kitchen layout</h2>
<div class="table-wrap"><table>
<thead><tr><th>Layout</th><th>Typical size</th><th>Indicative price</th></tr></thead>
<tbody>
<tr><td>Straight (one wall)</td><td>8–10 ft</td><td>₹1.2 – 2.5 lakh</td></tr>
<tr><td>L-shaped</td><td>10 × 8 ft</td><td>₹1.8 – 4 lakh</td></tr>
<tr><td>Parallel (galley)</td><td>2 × 9 ft</td><td>₹2.2 – 4.5 lakh</td></tr>
<tr><td>U-shaped</td><td>10 × 8 × 10 ft</td><td>₹3 – 5.5 lakh</td></tr>
<tr><td>Island</td><td>Open plan</td><td>₹4 – 7 lakh+</td></tr>
</tbody></table></div>
<p>These ranges include carcasses, shutters, counter, standard hardware and installation. Appliances such as the chimney, hob and built-in oven are extra.</p>
<h2>Price by shutter finish</h2>
<p>The shutter (door) finish is the biggest single choice after layout. Per square foot of kitchen, expect roughly:</p>
<ul>
<li><strong>Laminate:</strong> ₹1,200 – 1,800. Durable, easy to clean and the best value.</li>
<li><strong>Acrylic:</strong> ₹1,800 – 2,800. High gloss and a mirror-like look.</li>
<li><strong>PU paint:</strong> ₹2,500 – 4,000. Seamless matte or gloss in any colour.</li>
<li><strong>Veneer:</strong> ₹2,800 – 4,500. Real wood grain, lacquered for protection.</li>
</ul>
<h2>Five things that change the cost</h2>
<h3>1. Carcass material</h3>
<p>BWP (boiling water proof) plywood costs more than MR plywood or MDF, but it is the right choice for the sink area and anywhere near water. Read our <a href="{base}journal/plywood-guide-bwp-vs-mr/">plywood guide</a> to see where each grade belongs.</p>
<h3>2. Hardware</h3>
<p>Tandem drawers, corner carousels and tall pantry pull-outs make a kitchen far easier to use. Branded hardware such as Hettich adds cost but lasts for years.</p>
<h3>3. Counter top</h3>
<p>Granite is the most affordable. Quartz costs more but resists stains from turmeric and oil, which matters in an Indian kitchen.</p>
<h3>4. Number of tall units</h3>
<p>Floor-to-ceiling pantry and appliance units add a lot of storage and a lot of material. Each tall unit can add ₹25,000 to ₹60,000.</p>
<h3>5. Lighting and accessories</h3>
<p>Profile lights, glass shutters and internal organisers are small items that add up. Decide which ones you will use every day.</p>
<h2>How to plan your budget</h2>
<ol>
<li>Measure your kitchen and note where the window, gas line and drainage are.</li>
<li>Decide on the layout first, then the finish.</li>
<li>Keep 10% aside for appliances and last-minute changes.</li>
<li>Ask for a line-by-line quote so you can compare like for like.</li>
</ol>
<p>Prices in this guide are indicative for Ahmedabad in 2026 and vary with brand, design and site conditions. For an exact figure, <a href="{base}contact/">book a free site visit</a> and we'll measure and quote within a week.</p>
""",
    },
    {
        "slug": "plywood-guide-bwp-vs-mr",
        "title": "BWP vs MR plywood: which one belongs where in your home",
        "seo_title": "BWP vs MR Plywood: Which to Use for Kitchen & Wardrobe",
        "desc": "The difference between BWP, BWR and MR plywood, where each belongs in a home, and how to check plywood quality before your furniture is made.",
        "img": "W1",
        "date": "2026-08-27",
        "read": "5 min read",
        "excerpt": "Where waterproof plywood is worth it, where it isn't, and how to check what you're getting.",
        "body": """
<p>Plywood is hidden inside almost everything we build, from kitchen cabinets to beds. Choosing the right grade is one of the most important decisions in your interior, and one of the easiest to get wrong.</p>
<div class="callout"><b>Quick answer</b>Use BWP plywood in the kitchen, bathroom vanities and anywhere water may reach. MR plywood is fine for wardrobes, beds and furniture in dry rooms.</div>
<h2>The three grades you'll hear about</h2>
<div class="table-wrap"><table>
<thead><tr><th>Grade</th><th>Full name</th><th>Use it for</th></tr></thead>
<tbody>
<tr><td>MR</td><td>Moisture resistant (IS 303)</td><td>Wardrobes, beds, TV units in dry rooms</td></tr>
<tr><td>BWR</td><td>Boiling water resistant</td><td>Kitchens on a tighter budget</td></tr>
<tr><td>BWP</td><td>Boiling water proof (IS 710, marine)</td><td>Kitchens, sink units, vanities, utility areas</td></tr>
</tbody></table></div>
<h2>Why it matters in Ahmedabad</h2>
<p>Ahmedabad summers are dry, but the monsoon brings months of humidity, and kitchens see water every day. MR plywood near a sink can swell and delaminate within a few years. BWP plywood is bonded with waterproof resin and handles this far better.</p>
<h2>Where we use each grade</h2>
<ul>
<li><strong>Kitchen carcasses:</strong> BWP, always under the sink.</li>
<li><strong>Bathroom vanities:</strong> BWP.</li>
<li><strong>Wardrobes and lofts:</strong> MR or BWR, unless the wall is damp.</li>
<li><strong>Beds, TV units, study desks:</strong> MR is enough.</li>
<li><strong>Shutters with PU or veneer:</strong> BWP or good-quality MDF for a smooth finish.</li>
</ul>
<h2>How to check plywood quality</h2>
<ol>
<li>Look for the IS mark (IS 710 for BWP, IS 303 for MR) printed on each sheet.</li>
<li>Check the edges: layers should be even with no gaps or overlaps.</li>
<li>Ask for the brand and the invoice. A good maker will show you the sheets before cutting.</li>
<li>Knock on it. Good plywood sounds solid, not hollow.</li>
</ol>
<p>At our workshop you can see the plywood before we cut it. <a href="{base}contact/">Visit us in Vatva</a> or read about our <a href="{base}services/modular-kitchen-ahmedabad/">modular kitchens</a>.</p>
""",
    },
    {
        "slug": "3bhk-interior-design-ahmedabad",
        "title": "3BHK interior design in Ahmedabad: budget, timeline and ideas",
        "seo_title": "3BHK Interior Design in Ahmedabad: Cost, Timeline, Ideas",
        "desc": "Planning a 3BHK interior in Ahmedabad? Realistic budgets, a week-by-week timeline, and design ideas that make a flat feel larger and calmer.",
        "img": "L12",
        "date": "2026-07-30",
        "read": "7 min read",
        "excerpt": "Realistic budgets, a week-by-week timeline and ideas that make a flat feel larger.",
        "body": """
<p>A 3BHK is the most common home we design in Ahmedabad, from new towers in Shela and Gota to older flats in Maninagar and Paldi. Here's what to expect for budget, time and design.</p>
<div class="callout"><b>Quick answer</b>A complete 3BHK interior in Ahmedabad usually costs ₹8 lakh to ₹22 lakh and takes 8 to 12 weeks after the design is approved.</div>
<h2>Budget by scope</h2>
<div class="table-wrap"><table>
<thead><tr><th>Scope</th><th>What's included</th><th>Indicative budget</th></tr></thead>
<tbody>
<tr><td>Essential</td><td>Kitchen, three wardrobes, TV unit</td><td>₹5 – 8 lakh</td></tr>
<tr><td>Complete</td><td>Plus beds, false ceiling, lighting, paint</td><td>₹8 – 14 lakh</td></tr>
<tr><td>Premium</td><td>Plus veneer and PU finishes, panelling, loose furniture, curtains</td><td>₹14 – 22 lakh+</td></tr>
</tbody></table></div>
<h2>A realistic timeline</h2>
<ol>
<li><strong>Week 1:</strong> site visit, measurement and brief.</li>
<li><strong>Weeks 2–4:</strong> layouts, 3D views and material selection.</li>
<li><strong>Weeks 4–6:</strong> civil, electrical and false ceiling work at site.</li>
<li><strong>Weeks 4–10:</strong> kitchen, wardrobes and furniture made in the workshop.</li>
<li><strong>Weeks 10–12:</strong> installation, painting, cleaning and handover.</li>
</ol>
<h2>Ideas that make a 3BHK feel larger</h2>
<h3>Full-height storage</h3>
<p>Take wardrobes all the way to the ceiling and finish them in the wall colour. You get more storage and the room looks taller.</p>
<h3>One calm palette</h3>
<p>Choose two or three materials, for example warm white, one wood and one stone, and repeat them in every room. The home will feel connected and larger.</p>
<h3>Layered lighting</h3>
<p>Plan ceiling lights, wall lights and lamps on separate switches. Warm 2700–3000K light makes evenings feel relaxed.</p>
<h3>A proper pooja corner</h3>
<p>A well-designed mandir unit with storage for diyas and puja items keeps the area tidy and becomes a natural focal point.</p>
<h3>Plan the balcony</h3>
<p>In Ahmedabad, balconies are used year-round outside peak summer. A built-in bench and planters make it a real room.</p>
<p>See how we approached a similar home in <a href="{base}projects/satellite-residence/">Satellite Residence</a>, or explore our <a href="{base}services/residential-interior-design/">residential interiors</a> service.</p>
""",
    },
    {
        "slug": "sliding-vs-hinged-wardrobes",
        "title": "Sliding vs hinged wardrobes: how to choose for your room",
        "seo_title": "Sliding vs Hinged Wardrobe: Which Is Better? | SOC Interiors",
        "desc": "Sliding or hinged wardrobe doors? Compare space, cost, access and maintenance, with room-by-room advice from Ahmedabad wardrobe makers.",
        "img": "W8",
        "date": "2026-06-24",
        "read": "4 min read",
        "excerpt": "Space, cost, access and upkeep compared, with advice room by room.",
        "body": """
<p>Choosing between sliding and hinged doors changes how your bedroom feels and how easily you can use your wardrobe. Neither is always better. Here's how to decide.</p>
<div class="callout"><b>Quick answer</b>Choose sliding doors when the room is narrow or the bed is close to the wardrobe. Choose hinged doors when you want full access, lower cost and simpler upkeep.</div>
<h2>Side-by-side comparison</h2>
<div class="table-wrap"><table>
<thead><tr><th></th><th>Sliding</th><th>Hinged</th></tr></thead>
<tbody>
<tr><td>Space needed in front</td><td>None</td><td>About 2 ft to open</td></tr>
<tr><td>Access</td><td>Half the wardrobe at a time</td><td>Everything at once</td></tr>
<tr><td>Cost</td><td>10–20% more</td><td>Lower</td></tr>
<tr><td>Maintenance</td><td>Clean the tracks</td><td>Occasional hinge adjustment</td></tr>
<tr><td>Best width</td><td>6 ft and wider</td><td>Any width</td></tr>
</tbody></table></div>
<h2>Room-by-room advice</h2>
<ul>
<li><strong>Main bedroom:</strong> sliding, if the wardrobe faces the bed within 3 ft.</li>
<li><strong>Children's room:</strong> hinged, so children can reach everything easily.</li>
<li><strong>Guest room:</strong> hinged. It's simpler and costs less.</li>
<li><strong>Walk-in closet:</strong> open shelving or glass-front hinged doors.</li>
</ul>
<h2>Details that matter</h2>
<p>For sliding wardrobes, ask for a soft-close sliding system and an aluminium track. For hinged wardrobes, soft-close hinges stop slamming and protect the shutter. In both, plan internal drawers so they don't clash with the door when it opens.</p>
<p>See our <a href="{base}services/wardrobe-design-ahmedabad/">wardrobe service</a> or the walk-in closet in <a href="{base}projects/shela-penthouse/">Shela Penthouse</a>.</p>
""",
    },
]
