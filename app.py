"""
Local Price Finder

The browser sends a product name and a location.
This file looks them up in sample_data.py and returns a results page.
Prices there are Demo Data, not live shop prices.
"""

from flask import Flask, render_template, request

from sample_data import offers_for_shop, search_demo

app = Flask(__name__)


@app.route("/")
def home():
    """Show the search page."""
    return render_template("index.html")


@app.route("/search", methods=["GET", "POST"])
def search():
    """Find the same demo product at each sample shop and compare prices."""
    source = request.form if request.method == "POST" else request.args
    product = source.get("product", "").strip()
    location = source.get("location", "").strip()
    result = search_demo(product, location)
    return render_template(
        "results.html",
        product=product,
        location=location,
        groups=result["groups"],
        place_label=result["place_label"],
        used_default_place=result["used_default_place"],
    )


@app.route("/shop/<shop_id>")
def shop(shop_id):
    """Show one sample shop and the demo products it sells."""
    location = request.args.get("location", "").strip()
    result = search_demo("", location)
    # search_demo with an empty product returns no groups, but we only need the place.
    # Recompute the origin the same way by searching a known product if needed.
    from sample_data import find_place, PLACES

    place = find_place(location)
    origin = place[1] if place else PLACES["mg road"]
    details = offers_for_shop(shop_id, origin)
    if details is None:
        return render_template("shop.html", missing=True, location=location), 404
    return render_template(
        "shop.html",
        missing=False,
        location=location,
        place_label=result["place_label"],
        **details,
    )


if __name__ == "__main__":
    # Port 5001, because another program on this computer is already using 5000.
    app.run(debug=True, port=5001)
