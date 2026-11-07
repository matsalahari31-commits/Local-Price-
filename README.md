# Local Price Finder

A beginner project that will compare sample shop prices for the same product.

**Important:** Prices in this project start as **Demo Data**. They are made-up examples so you can learn. They are not live prices from real shops.

## What we are building (later steps)

1. A simple homepage with a search box
2. Sample products and shops
3. Search
4. Price comparison
5. Sorting from lowest price to highest
6. Location and distance
7. A SQLite database
8. A cleaner page design
9. A plan for connecting real shop data later

## Step 1 — project setup (done in this step)

```
local-price-finder/
├── app.py                 # starts the website
├── requirements.txt       # lists the Python tools we need
├── README.md              # this explanation
├── database/              # the database file will go here in a later step
├── templates/             # HTML pages will go here
└── static/                # CSS and JavaScript will go here
```

## Words you will see

| Word | Simple meaning |
| --- | --- |
| HTML | The text and structure of a web page |
| CSS | How the page looks (colors, spacing) |
| JavaScript | Extra behavior in the browser (we add this later) |
| Python | The language used for the server |
| Flask | A small Python tool that serves web pages |
| SQLite | A simple database stored in one file (added later) |
| Demo Data | Fake sample prices for learning, not real shop prices |

## How to run Step 1

Open a terminal in the `local-price-finder` folder, then run these commands one at a time.

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python app.py
```

Then open a browser and go to:

http://127.0.0.1:5000

You should see the heading **Local Price Finder** and the line **Step 1 is working.**

To stop the site, click the terminal and press `Ctrl + C`.
