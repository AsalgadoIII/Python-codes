from flask import Flask, render_template_string

app = Flask(__name__)

FEATURED_PIECES = [
    {
        "name": "Luna Orbit Ear Stack",
        "description": "Mixed metals + cubic zirconia slices to fake a full ear stack without extra piercings.",
        "price": "$58",
        "link": "https://example.com/luna-orbit",
        "mood": "Night-out glow",
        "tags": ["Stacked", "Mixed Metal", "CZ"]
    },
    {
        "name": "Opal Nova Pendant",
        "description": "Lab opal cabochon suspended in a 18k gold vermeil bezel, paired with a satellite chain.",
        "price": "$72",
        "link": "https://example.com/opal-nova",
        "mood": "Soft girl aura",
        "tags": ["Opal", "Gold", "Layerable"]
    },
    {
        "name": "Galaxy Beaded Friendship Set",
        "description": "Pair of hand-strung gemstone bracelets with customizable charms for BFF swaps.",
        "price": "$44",
        "link": "https://example.com/galaxy-bff",
        "mood": "Everyday sparkle",
        "tags": ["Gemstone", "Gift", "Custom"]
    }
]

TEMPLATE = """
<!doctype html>
<html lang=\"en\">
<head>
  <meta charset=\"utf-8\">
  <title>ShineScout — Jewelry Radar</title>
  <style>
    body { font-family: 'Poppins', Arial, sans-serif; background: #0b1120; color: #f1f5f9; padding: 2rem; }
    h1 { margin: 0; font-size: 2.4rem; }
    p.sub { color: #cbd5f5; margin-top: 0.3rem; }
    .grid { display: grid; gap: 1.5rem; grid-template-columns: repeat(auto-fit,minmax(280px,1fr)); margin-top: 2rem; }
    .card { background: rgba(15,23,42,0.8); border: 1px solid rgba(148,163,184,0.2); border-radius: 1.2rem; padding: 1.5rem; }
    .price { font-weight: 600; color: #fbbf24; }
    .mood { text-transform: uppercase; font-size: 0.75rem; letter-spacing: 0.1em; color: #a5b4fc; }
    .tags { margin-top: 0.5rem; }
    .tag { display: inline-block; margin-right: 0.35rem; padding: 0.2rem 0.6rem; border-radius: 999px; background: rgba(56,189,248,0.2); color: #38bdf8; font-size: 0.75rem; }
    a.cta { display: inline-flex; align-items: center; margin-top: 0.8rem; color: #34d399; text-decoration: none; font-weight: 600; }
    a.cta:hover { text-decoration: underline; }
  </style>
</head>
<body>
  <h1>ShineScout</h1>
  <p class=\"sub\">Curated jewelry picks for the 22-year-old trendsetter in your life.</p>
  <div class=\"grid\">
    {% for piece in pieces %}
      <div class=\"card\">
        <div class=\"mood\">{{ piece.mood }}</div>
        <h2>{{ piece.name }}</h2>
        <p>{{ piece.description }}</p>
        <div class=\"price\">{{ piece.price }}</div>
        <div class=\"tags\">
          {% for tag in piece.tags %}
            <span class=\"tag\">{{ tag }}</span>
          {% endfor %}
        </div>
        <a class=\"cta\" href=\"{{ piece.link }}\" target=\"_blank\">Shop this look →</a>
      </div>
    {% endfor %}
  </div>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(TEMPLATE, pieces=FEATURED_PIECES)

if __name__ == '__main__':
    app.run(debug=True)
