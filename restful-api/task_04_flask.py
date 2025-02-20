from flask import Flask, jsonify, request

app = Flask(__name__)

# Dictionary to store user data
users = {
    "jane": {
        "username": "jane",
        "name": "Jane",
        "age": 28,
        "city": "Los Angeles"
    },
    "john": {
        "username": "john",
        "name": "John",
        "age": 30,
        "city": "New York"
    },
}


@app.route("/")
def home():
    """Return a welcome message for the API."""
    return "Welcome to the Flask API!"


@app.route("/data")
def get_usernames():
    """Return a list of all usernames stored in the API."""
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    """Return a status message indicating API is running."""
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    """Retrieve user details based on username.

    Args:
        username (str): The username of the user to retrieve.

    Returns:
        JSON response containing user data or an error message.
    """
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """Add a new user to the API.

    Expects a JSON payload with 'username', 'name', 'age', and 'city'.

    Returns:
        JSON response confirming user addition or an error message.
    """
    data = request.get_json()

    if not data or "username" not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data["username"]

    if username in users:
        return jsonify({"error": "User already exists"}), 400

    users[username] = {
        "username": username,
        "name": data.get("name", ""),
        "age": data.get("age", 0),
        "city": data.get("city", "")
    }

    return jsonify({"message": "User added", "user": users[username]}), 201


if __name__ == "__main__":
    app.run(debug=True)
