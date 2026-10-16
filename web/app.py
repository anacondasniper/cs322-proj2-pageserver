from flask import Flask, render_template, request, abort
from jinja2 import TemplateNotFound

app = Flask(__name__)

@app.route('/index')
def hello():
    name = request.args.get("nameRequest")
    if name is None: name = "Test"
    return render_template("index.html", htmlName=name), 200

@app.route('/<page>')
def serve(page):
    if ".." in page or "//" in page or "~" in page or page.startswith("/"):
        abort(403)
    try:
        return render_template(page), 200
    except TemplateNotFound:
        abort(404)

@app.errorhandler(404)
def error_404(e):
    return render_template("404.html"), 404

@app.errorhandler(403)
def error_403(e):
    return render_template("403.html"), 403

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
