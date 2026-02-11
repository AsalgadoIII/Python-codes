# AI Trend App – 2026-02-11

**ShineScout** is a quick-build web app inspired by the current jewelry micro-trend for Gen Z shoppers. It showcases a rotating trio of standout pieces with story-driven blurbs, perfect for sharing with someone who loves jewelry.

## Concept
- **Trend**: Etsy/TikTok surges in handmade gemstone jewelry and mixed-metal ear stacks for women in their early 20s.
- **Goal**: Present curated picks with mood tags, pricing, and CTA links that can be swapped daily.

## Stack
- Python 3.11
- Flask 3
- Static JSON data (placeholder; swap with live feed later)

## Run Locally
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```
Visit <http://127.0.0.1:5000> to view the app.

## Next Steps
- Hook into live jewelry feeds (Etsy, Instagram shops) via API/scraper.
- Add shareable wish-list links + affiliate tags.
- Deploy to Vercel/Fly.io for frictionless sharing.
