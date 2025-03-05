from app import app
from flask import request, jsonify, Response

# Static route
@app.route("/")
def home():
    return "Hello, Flask!"

# Dynamic route
@app.route("/user/<name>")
def show_user(name):
    return f"Hello, {name}"

@app.route("/post/<int:post_id>")
def show_post(post_id):
    return f"Post ID: {post_id}"

# Query parameters
@app.route("/search")
def search():
    query = request.args.get("query")
    return f"Search results: {query}"

# HTTP methods
# GET - Used to read data
@app.route("/greet", methods=["GET"])
def greet():
    name = request.args.get("name", "Guest")
    return f"Hello, {name}"

# POST - Sending data
@app.route("/signup", methods=["POST"])
def submit_form():
    username = request.form.get("username")
    
    return f"Form submitted!, Welcome {username}"

# Flask can also handle JSON requests
@app.route("/json", methods=["POST"])
def handle_json():
    # Parses the json to normal python dict
    data = request.json
    
    name = data.get("name")
    age = data.get("age")
    
    # Flask provides a Response object to give fine-grained control over responses.
    response = Response("Custom response test", status=202, mimetype="text/plain")
    
    # jsonify serializes the dict into a JSON format
    return jsonify({"message": f"Hello. {name}! You are {age} years old"})