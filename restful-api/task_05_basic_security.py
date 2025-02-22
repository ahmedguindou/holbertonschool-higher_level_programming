#!/usr/bin/python3
"""API Security and Authentication Techniques"""
from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity
from flask_jwt_extended import JWTManager, create_access_token


app = Flask(__name__)

# Configure JWT
app.config['JWT_SECRET_KEY'] = 'supersecretkey'
jwt = JWTManager(app)

# Set up Basic Auth
auth = HTTPBasicAuth()

# In-memory user data (Replace with a database in production)
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


# Verify Password for Basic Authentication
@auth.verify_password
def verify_password(username, password):
    """Verify if the username and password are correct."""
    if username in users and check_password_hash(
            users[username]["password"], password):
        return username
    return None


# Basic Auth Protected Route
@app.route('/basic-protected', methods=['GET'])
@auth.login_required
def basic_protected():
    """Protected route with basic authentication."""
    return jsonify({"message": "Basic Auth: Access Granted"})


# Login Route for JWT Authentication
@app.route('/login', methods=['POST'])
def login():
    """Login route to generate a JWT token."""
    data = request.get_json()

    if not data or not data.get('username') or not data.get('password'):
        return jsonify({"error": "Username and password required"}), 400

    username = data.get('username')
    password = data.get('password')

    if username in users and check_password_hash(
            users[username]['password'], password):
        access_token = create_access_token(
            identity={"username": username, "role": users[username]["role"]}
        )
        return jsonify(access_token=access_token)

    return jsonify({"error": "Invalid credentials"}), 401


# JWT Auth Protected Route
@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def jwt_protected():
    """Protected route with JWT authentication."""
    return jsonify({"message": "JWT Auth: Access Granted"})


# Admin-only Route with Role-based Access Control
@app.route('/admin-only', methods=['GET'])
@jwt_required()
def admin_only():
    """Admin-only route with role-based access control."""
    user = get_jwt_identity()
    if user["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return jsonify({"message": "Admin Access: Granted"})


# Custom JWT Error Handlers
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """Handle unauthorized error for JWT."""
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """Handle invalid token error."""
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    """Handle expired token error."""
    return jsonify({"error": "Token has expired"}), 401


if __name__ == '__main__':
    app.run(debug=True)
