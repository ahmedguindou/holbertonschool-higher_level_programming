from flask import Flask
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    "user1": generate_password_hash("password"),
    "admin1": generate_password_hash("password")
}


@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if user and check_password_hash(user, password):
        return username
    return None


@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"


if __name__ == '__main__':
    app.run()
