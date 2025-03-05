from flask import Flask, request

app = Flask(__name__)

# Static route
@app.route("/")
def home():
    return "Hello, Flask!"

# Dynamic route
"""
Flask allows us to pass data in the URL using parameters and query strings.

🔹 URL Parameters (<variable>)
These are dynamic values in a URL.
You define them in the route using <variable_name>.
Flask extracts them and passes them as function arguments.

"""
@app.route("/user/<name>")
def show_user(name):
    return f"Hello, {name}"

## You can specify data types for URL params
@app.route("/post/<int:post_id>")
def show_post(post_id):
    return f"Post ID: {post_id}"

# Query Strings - These are optional parameters sent in the URL after a ?.
# Multiple values are separated by &.
@app.route("/search")
def search():
    query = request.args.get("query")
    return f"Search results: {query}"

if __name__ == "__main__":
    app.run(debug=True)
