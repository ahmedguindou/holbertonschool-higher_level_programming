#!/usr/bin/python3
"""
Basic Security Implementation with Flask
This app demonstrates Basic Authentication (HTTPBasicAuth) and JWT (JSON Web Token) Authentication,
with role-based access control (Admin-only route).
"""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token
from flask_jwt_extended import jwt_required, get_jwt_identity

app = Flask(__name__)
auth = HTTPBasicAuth()
jwt = JWTManager(app)
app.config['SECRET_KEY'] = 'your_secret_key'

# User data with hashed passwords and roles
users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
}


@auth.verify_password
def verify_password(username, password):
    """Verify the username and password for Basic Authentication."""
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        return username
    return None


@app.route('/login', methods=['POST'])
def login():
    """Login and return a JWT token if credentials are valid."""
    username = request.json.get('username')
    password = request.json.get('password')
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        access_token = create_access_token(identity={"username": username, "role": user["role"]})
        return jsonify(access_token=access_token)
    return jsonify({"error": "Invalid credentials"}), 401


@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    """Protected route using Basic Authentication."""
    return "Basic Auth: Access Granted"


@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    """Protected route using JWT Authentication."""
    return "JWT Auth: Access Granted"


@app.route('/admin-only')
@jwt_required()
def admin_only():
    """Admin-only route, protected by JWT and role check."""
    user = get_jwt_identity()
    if user.get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """Handle missing or invalid token errors."""
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """Handle invalid token error."""
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    """Handle expired token error."""
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    """Handle revoked token error."""
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    """Handle fresh token required error."""
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == '__main__':
    app.run()
