from flask import Flask, jsonify, request

# Instantiate the Flask application
app = Flask(__name__)

# Dictionary to store users
users = {
    "jane": {
        "username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"
    },
    "john": {
        "username": "john", "name": "John", "age": 30, "city": "New York"
    },
}


@app.route("/")
def home():
    """Handles the root endpoint to display a welcome message."""
    return "Welcome to the Flask API!"


@app.route("/data")
def get_usernames():
    """Returns a list of all usernames stored in the users dictionary."""
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    """Returns 'OK' status message."""
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    """Returns the full object for a given username."""
    user = users.get(username)

    if user:
        return jsonify(user)

    return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """Adds a new user to the users dictionary based on the posted data."""
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


# Start the Flask application
if __name__ == "__main__":
    app.run()
