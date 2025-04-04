from flask import request, jsonify, Response, render_template, url_for, flash,session, redirect, Blueprint
# Flask WTF is used to manage forms
from flask_wtf import FlaskForm 
from wtforms import StringField, SubmitField , EmailField
from wtforms.validators import DataRequired, Email # This ensures the field is not left empty.
from .models import db, User

routes = Blueprint("routes", __name__)

# Static route
@routes.route("/")
def home():
    return render_template("home.html")

# Dynamic route
@routes.route("/user/<name>")
def show_user(name):
    ## Flask accepts any DS to be passed to the template
    ## This can be a simple list, dict etc
    students = ["Paul Murithi", "Ashley Koech", "Mily Cyrus", "Joel Kaizer"]
    print(students)
    return render_template("home.html", data=students)

@routes.route("/post/<int:post_id>")
def show_post(post_id):
    return f"Post ID: {post_id}"

# Query parameters
@routes.route("/search")
def search():
    query = request.args.get("query")
    return f"Search results: {query}"

# HTTP methods
# GET - Used to read data
@routes.route("/greet", methods=["GET"])
def greet():
    name = request.args.get("name", "Guest")
    return f"Hello, {name}"

# POST - Sending data
@routes.route("/signup", methods=["POST"])
def submit_form():
    username = request.form.get("username")
    
    return f"Form submitted!, Welcome {username}"

# Flask can also handle JSON requests
@routes.route("/json", methods=["POST"])
def handle_json():
    # Parses the json to normal python dict
    data = request.json
    
    name = data.get("name")
    age = data.get("age")
    
    # Flask provides a Response object to give fine-grained control over responses.
    response = Response("Custom response test", status=202, mimetype="text/plain")
    
    # jsonify serializes the dict into a JSON format
    return jsonify({"message": f"Hello. {name}! You are {age} years old"})

# Flask Forms
"""
Flask doesn’t have built-in form handling, so we use Flask-WTF (a wrapper around WTForms) to manage forms.
"""

# Base class for WTF. Defined class will inherit from this class
class MyForm(FlaskForm):
    # StringField: Represents a text input field. It takes the field label (e.g., 'Name') and a list of validators (e.g., DataRequired()).
    name = StringField('Enter your name', validators=[DataRequired("Name is required")])
    email = EmailField("Enter your Email", validators=[DataRequired(), Email()])
    # SubmitField: Represents a submit button on the form.
    submit = SubmitField("Submit")
    
@routes.route("/sign-up")
def handle_sign_up():
    form = MyForm()
    if form.validate_on_submit(): # Check if form is submitted and valid
        name = form.name.data # GEt form data
        return f"Thankyou for signing up {name}"
    return render_template("auth.html", form = form) # Render the template

## Flash Messages in Flask
# Flash messages are used to display temporary notifications like success, errors, or warnings.
# They disappear after one request-response cycle (after reloading or navigating).
@routes.route("/submit", methods=["POST"])
def submit():
    flash("Form Submitted succesfully", "success")
    return redirect(url_for("sign-up"))

@routes.route("/add_user", methods=["POST"])
def add_user():
    data = request.get_json()
    username = data.get("username")
    email = data.get("email")

    if not username or not email:
        return jsonify({"error": "Username and email are required"}), 400

    user = User(username=username, email=email)
    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "User added successfully", "user": {"id": user.id, "username": user.username, "email": user.email}}), 201