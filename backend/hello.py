from app import app
from markupsafe import escape

@app.route("/")
def hello_world():
    return "<p>Hello, World sdL" 