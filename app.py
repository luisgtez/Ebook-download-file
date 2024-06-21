from flask import Flask, send_file, render_template
import os
from urllib.parse import unquote

app = Flask(__name__)

BOOKS_PATH = "Books"

@app.route("/")
def root():
    files = os.listdir(BOOKS_PATH)
    files.sort(key=lambda f: os.path.getmtime(os.path.join(BOOKS_PATH, f)), reverse=True)
    return render_template("index.html", files=files)

@app.route("/books/<path:filename>")
def get_book(filename):
    filename = unquote(filename)
    return send_file(os.path.join(BOOKS_PATH, filename), as_attachment=True)

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=5001)
