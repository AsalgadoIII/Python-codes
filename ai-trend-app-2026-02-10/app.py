from flask import Flask, render_template_string

app = Flask(__name__)

TOOLS = [
    {
        "name": "FlowPilot",
        "summary": "Auto-builds SOP bots from your Looms and Notion docs.",
        "cta": "https://example.com/flowpilot",
        "signal": "Trending on X + HackerNews"
    },
    {
        "name": "PromptBench",
        "summary": "Test prompts across GPT, Claude, Gemini in one dashboard.",
        "cta": "https://example.com/promptbench",
        "signal": "Top AI indie launch today"
    },
    {
        "name": "MacroMind",
        "summary": "GPT-powered spreadsheet co-pilot for finance teams.",
        "cta": "https://example.com/macromind",
        "signal": "Gaining traction in AI productivity circles"
    }
]

TEMPLATE = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>AI Productivity Toolkit Radar</title>
  <style>
    body { font-family: Arial, sans-serif; padding: 2rem; background: #0f172a; color: #f8fafc; }
    h1 { margin-bottom: 0.25rem; }
    p.sub { color: #94a3b8; margin-top: 0; }
    .card { background: #1e293b; padding: 1.5rem; border-radius: 1rem; margin-bottom: 1rem; }
    a { color: #38bdf8; text-decoration: none; font-weight: bold; }
    .signal { font-size: 0.85rem; color: #c084fc; text-transform: uppercase; letter-spacing: 0.08em; }
  </style>
</head>
<body>
  <h1>AI Productivity Toolkit Radar</h1>
  <p class="sub">Auto-generated showcase of today's trending build-in-public tools.</p>
  {% for tool in tools %}
    <div class="card">
      <div class="signal">{{ tool.signal }}</div>
      <h2>{{ tool.name }}</h2>
      <p>{{ tool.summary }}</p>
      <a href="{{ tool.cta }}" target="_blank">Check it out →</a>
    </div>
  {% endfor %}
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(TEMPLATE, tools=TOOLS)

if __name__ == "__main__":
    app.run(debug=True)
