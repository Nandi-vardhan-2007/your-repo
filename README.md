# Render-ready YouTube Downloader (Glassmorphism UI - C4)

This is a minimal Flask app using `yt-dlp` for downloading videos.
The UI is a glassmorphism-styled page (option C4 you picked).

## Quick notes (read this unless you enjoy surprises)
- Deploying a public YouTube downloader may violate YouTube's Terms of Service. Use responsibly and only for personal or permitted content.
- Long downloads might time out on free hosts. For production use, add background job processing (Redis + RQ / Celery) or use chunked downloads with progress.
- Render free plan may sleep on inactivity and impose request/response time limits.

## Local testing
1. Create a virtualenv and activate it.
2. `pip install -r requirements.txt`
3. `python app.py`
4. Open http://localhost:5000 in your browser.

## Deploy to Render
1. Push this repository to GitHub (or GitLab).
2. On Render dashboard, create a new **Web Service**.
3. Connect your repo, branch.
4. Set Environment to **Python**.
5. Build Command: `pip install -r requirements.txt`
6. Start Command: `gunicorn app:app`
7. Add any environment variables if you want to override `FLASK_SECRET`.

## Files in this project
- `app.py` - Flask app
- `downloader.py` - wrapper around yt-dlp
- `templates/index.html` - glassmorphism UI
- `static/style.css` - styles for the UI
- `render.yaml`, `Procfile`, `requirements.txt`

## Improvements to make it production-ready
- Add authentication or API key to avoid abuse.
- Move downloads to ephemeral object storage (S3) instead of local disk.
- Run downloads asynchronously; return a job id and let client poll.
- Add rate-limiting / captcha.
