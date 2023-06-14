from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField
from wtforms.validators import DataRequired

# Create our Flask Instance

app = Flask(__name__)
app.config['TESTING'] = True
app.config['SECRET_KEY'] = "super secret key to be added in future in a more secure way"

# Create URL Routes

@app.route("/")
def index():
# return "<h1>Hello, World!</h1>"
     return render_template("index.html")


@app.route("/about")
def about():
     return render_template("about.html")

@app.route("/login", methods=['GET', 'POST'] )
def login():
     email = None
     form = LoginForm()
     #validate 
     if form.validate_on_submit():
          email = form.email.data
          form.email.data = ''
          flash("Form submitted successfully")
     return render_template("login.html", email = email, form = form)


@app.errorhandler(404)
def page_not_found(e):
     return render_template("404.html"), 404


@app.errorhandler(500)
def server_error(e):
     return render_template("server_error.html"), 500

# Forms
# create a form class
class LoginForm(FlaskForm):
     email = EmailField("Email", validators=[DataRequired()])
     submit = SubmitField("Submit")



