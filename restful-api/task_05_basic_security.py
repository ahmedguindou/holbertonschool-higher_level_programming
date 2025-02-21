from flask import Flask, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity
)

# Initialize Flask app
app = Flask(__name__)

# Configure the secret key for JWT
app.config['JWT_SECRET_KEY'] = 'ahmed'

# Initialize HTTPBasicAuth and JWTManager
auth = HTTPBasicAuth()
jwt = JWTManager(app)

# Sample users stored in memory
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


# Basic Authentication: Verify username and password
@auth.verify_password
def verify_password(username, password):
    if (username in users and
            check_password_hash(users[username]["password"], password)):
        return users[username]
    return None


# Basic Auth Protected Route
@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"


# JWT Authentication: Login route
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username', '')
    password = data.get('password', '')

    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        # Create a JWT token and embed user role in the claims
        access_token = create_access_token(
            identity=username,
            additional_claims={"role": user["role"]}
        )
        return jsonify(access_token=access_token)

    return jsonify({"error": "Invalid credentials"}), 401


# JWT Protected Route
@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"


# Role-based Access Control: Admin-only route
@app.route('/admin-only')
@jwt_required()
def admin_only():
    claims = get_jwt_identity()
    if claims.get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"


# Custom error handlers for JWT-related errors
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401


# Run the app
if __name__ == '__main__':
    app.run(debug=True)
