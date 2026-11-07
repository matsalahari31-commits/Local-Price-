"""
Sample shops and prices for learning.

Every price in this file is Demo Data. These are made-up numbers
so the website can run without a paid shop API. They are not live prices.
"""

import math

# A place name the user might type, and a sample map point (latitude, longitude).
PLACES = {
    "mg road": (12.9756, 77.6068),
    "mahatma gandhi road": (12.9756, 77.6068),
    "indiranagar": (12.9784, 77.6408),
    "koramangala": (12.9352, 77.6245),
    "jayanagar": (12.9308, 77.5838),
    "bengaluru": (12.9716, 77.5946),
    "bangalore": (12.9716, 77.5946),
}

SHOPS = [
    {
        "id": "abc",
        "name": "ABC Supermarket",
        "address": "42 MG Road, Bengaluru",
        "area": "MG Road",
        "lat": 12.9762,
        "lng": 77.6074,
        "opens": "8:00 AM",
        "closes": "10:00 PM",
    },
    {
        "id": "fresh",
        "name": "Fresh Basket",
        "address": "18 100 Feet Road, Indiranagar, Bengaluru",
        "area": "Indiranagar",
        "lat": 12.9789,
        "lng": 77.6412,
        "opens": "7:30 AM",
        "closes": "9:30 PM",
    },
    {
        "id": "city",
        "name": "City Mart",
        "address": "7 80 Feet Road, Koramangala, Bengaluru",
        "area": "Koramangala",
        "lat": 12.9348,
        "lng": 77.6238,
        "opens": "9:00 AM",
        "closes": "9:00 PM",
    },
    {
        "id": "daily",
        "name": "Daily Needs",
        "address": "15 4th Block, Jayanagar, Bengaluru",
        "area": "Jayanagar",
        "lat": 12.9299,
        "lng": 77.5831,
        "opens": "8:30 AM",
        "closes": "9:30 PM",
    },
]

# One record is one exact product: same brand, name, and size.
# A 5kg bag is not the same product as a 1kg bag.
PRODUCTS = [
    {
        "id": "rice-5kg",
        "name": "Basmati Rice",
        "brand": "India Gate",
        "quantity": "5kg",
        "keywords": "rice basmati 5kg 5 kg",
    },
    {
        "id": "rice-1kg",
        "name": "Basmati Rice",
        "brand": "India Gate",
        "quantity": "1kg",
        "keywords": "rice basmati 1kg 1 kg",
    },
    {
        "id": "milk-1l",
        "name": "Toned Milk",
        "brand": "Nandini",
        "quantity": "1 litre",
        "keywords": "milk 1 litre 1l liter",
    },
    {
        "id": "shampoo-650",
        "name": "Daily Shine Shampoo",
        "brand": "Dove",
        "quantity": "650ml",
        "keywords": "shampoo 650ml 650 ml",
    },
    {
        "id": "laptop-dell",
        "name": "Inspiron 15",
        "brand": "Dell",
        "quantity": "15 inch, 8GB RAM",
        "keywords": "laptop computer dell inspiron",
    },
    {
        "id": "phone-a15",
        "name": "Galaxy A15",
        "brand": "Samsung",
        "quantity": "128GB",
        "keywords": "mobile phone smartphone samsung galaxy",
    },
]

# price is in rupees. available is yes or no for this demo.
OFFERS = [
    {"product_id": "rice-5kg", "shop_id": "abc", "price": 620, "available": True},
    {"product_id": "rice-5kg", "shop_id": "fresh", "price": 590, "available": True},
    {"product_id": "rice-5kg", "shop_id": "city", "price": 650, "available": True},
    {"product_id": "rice-5kg", "shop_id": "daily", "price": 610, "available": False},
    {"product_id": "rice-1kg", "shop_id": "abc", "price": 145, "available": True},
    {"product_id": "rice-1kg", "shop_id": "fresh", "price": 132, "available": True},
    {"product_id": "rice-1kg", "shop_id": "city", "price": 150, "available": True},
    {"product_id": "milk-1l", "shop_id": "abc", "price": 46, "available": True},
    {"product_id": "milk-1l", "shop_id": "fresh", "price": 44, "available": True},
    {"product_id": "milk-1l", "shop_id": "city", "price": 48, "available": False},
    {"product_id": "milk-1l", "shop_id": "daily", "price": 45, "available": True},
    {"product_id": "shampoo-650", "shop_id": "abc", "price": 399, "available": True},
    {"product_id": "shampoo-650", "shop_id": "fresh", "price": 375, "available": True},
    {"product_id": "shampoo-650", "shop_id": "city", "price": 420, "available": True},
    {"product_id": "laptop-dell", "shop_id": "abc", "price": 52990, "available": True},
    {"product_id": "laptop-dell", "shop_id": "city", "price": 51490, "available": True},
    {"product_id": "laptop-dell", "shop_id": "daily", "price": 53990, "available": False},
    {"product_id": "phone-a15", "shop_id": "abc", "price": 17499, "available": True},
    {"product_id": "phone-a15", "shop_id": "fresh", "price": 16999, "available": True},
    {"product_id": "phone-a15", "shop_id": "city", "price": 17999, "available": True},
]


def rupees(amount):
    """Turn 16999 into ₹16,999."""
    text = f"{amount:,}"
    return "₹" + text


def normalize(text):
    cleaned = text.lower().replace("-", " ").replace(",", " ")
    return " ".join(cleaned.split())


def find_place(location_text):
    """Pick the most specific demo place named in the user's text."""
    lowered = normalize(location_text)
    found = None
    for name, coords in PLACES.items():
        if name in lowered and (found is None or len(name) > len(found[0])):
            found = (name, coords)
    return found


def distance_km(start, end):
    """Straight-line sample distance between two map points, in kilometres."""
    lat1, lon1 = math.radians(start[0]), math.radians(start[1])
    lat2, lon2 = math.radians(end[0]), math.radians(end[1])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    haversine = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    return 6371 * 2 * math.asin(math.sqrt(haversine))


def product_matches(product, query):
    """True when the search words fit this exact brand, name, and size."""
    query_text = normalize(query)
    if not query_text:
        return False

    blob = normalize(
        " ".join([product["name"], product["brand"], product["quantity"], product["keywords"]])
    )
    compact_blob = blob.replace(" ", "")
    compact_query = query_text.replace(" ", "")

    if compact_query in compact_blob:
        return True

    words = blob.split()
    return all(word in words or word in compact_blob for word in query_text.split())


def search_demo(query, location_text):
    """Return matching products, each with its own shop list sorted by price."""
    place = find_place(location_text)
    if place is None:
        origin = PLACES["mg road"]
        place_label = "MG Road (demo default)"
        used_default = True
    else:
        origin = place[1]
        place_label = place[0].title()
        used_default = False

    shops_by_id = {shop["id"]: shop for shop in SHOPS}
    groups = []

    for product in PRODUCTS:
        if not product_matches(product, query):
            continue

        rows = []
        for offer in OFFERS:
            if offer["product_id"] != product["id"]:
                continue
            shop = shops_by_id[offer["shop_id"]]
            kilometres = distance_km(origin, (shop["lat"], shop["lng"]))
            rows.append(
                {
                    "shop": shop,
                    "price": offer["price"],
                    "price_label": rupees(offer["price"]),
                    "available": offer["available"],
                    "availability_label": "In stock" if offer["available"] else "Out of stock",
                    "distance_km": round(kilometres, 1),
                }
            )

        rows.sort(key=lambda row: row["price"])
        if not rows:
            continue

        lowest = rows[0]["price"]
        highest = rows[-1]["price"]
        best = rows[0]
        for row in rows:
            row["is_lowest"] = row["price"] == lowest

        groups.append(
            {
                "product": product,
                "rows": rows,
                "best": best,
                "lowest_label": rupees(lowest),
                "highest_label": rupees(highest),
                "difference_label": rupees(highest - lowest),
                "savings_label": rupees(highest - lowest),
            }
        )

    return {
        "groups": groups,
        "place_label": place_label,
        "used_default_place": used_default,
    }


def get_shop(shop_id):
    for shop in SHOPS:
        if shop["id"] == shop_id:
            return shop
    return None


def offers_for_shop(shop_id, origin):
    """All demo products sold by one shop, for the shop details page."""
    products_by_id = {product["id"]: product for product in PRODUCTS}
    shop = get_shop(shop_id)
    if shop is None:
        return None

    items = []
    for offer in OFFERS:
        if offer["shop_id"] != shop_id:
            continue
        product = products_by_id[offer["product_id"]]
        items.append(
            {
                "product": product,
                "price_label": rupees(offer["price"]),
                "availability_label": "In stock" if offer["available"] else "Out of stock",
            }
        )
    items.sort(key=lambda item: item["product"]["name"])
    return {
        "shop": shop,
        "distance_km": round(distance_km(origin, (shop["lat"], shop["lng"])), 1),
        "items": items,
    }
