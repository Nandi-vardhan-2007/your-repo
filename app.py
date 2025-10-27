from flask import Flask, request, render_template, send_file, redirect, url_for, flash
from downloader import download_video
import glob, os, time
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET', 'please-change-me')

DOWNLOAD_DIR = os.path.join(os.getcwd(), 'downloads')
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    url = request.form.get('url','').strip()
    if not url:
        flash('Provide a YouTube URL, genius.')
        return redirect(url_for('index'))

    # sanitize filename later; yt-dlp will write to downloads/
    try:
        download_video(url, DOWNLOAD_DIR)
    except Exception as e:
        # yt-dlp prints useful errors; surface a friendly message
        flash(f'Download failed: {e}')
        return redirect(url_for('index'))

    # pick the most recent file in downloads
    files = glob.glob(os.path.join(DOWNLOAD_DIR, '*'))
    if not files:
        flash('No file found after download. Something broke.')
        return redirect(url_for('index'))

    latest = max(files, key=os.path.getctime)
    return send_file(latest, as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=False)
