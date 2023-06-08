from flask import Flask, render_template

# Create our Flask Instance

app = Flask(__name__)
app.config['TESTING'] = True

# Create URL Routeshello

@app.route("/")
def index():
# return "<h1>Hello, World!</h1>"
     return render_template("index.html")


@app.route("/about")
def about():
     return render_template("about.html")


@app.errorhandler(404)
def page_not_found(e):
     return render_template("404.html"), 404


@app.errorhandler(500)
def server_error(e):
     return render_template("server_error.html"), 500
