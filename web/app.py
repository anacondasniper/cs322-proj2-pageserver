from flask import Flask, render_template, send_from_directory, request, abort
from jinja2 import TemplateNotFound

app = Flask(__name__)
app.url_map.merge_slashes = False

@app.route('/index')
def hello():
    name = request.args.get("nameRequest", "Test")
    return render_template("index.html", htmlName=name), 200

@app.route('/<path:page>')
def serve(page):
    if ".." in page or "//" in page or "~" in page or page.startswith("/"):
        abort(403)
    return send_from_directory("templates", page)
    
@app.errorhandler(404)
def error_404(e):
    return render_template("404.html"), 404

@app.errorhandler(403)
def error_403(e):
    return render_template("403.html"), 403

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
