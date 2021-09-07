from flask import Flask, current_app, request, jsonify
from lihim import controller

app = Flask(__name__, static_folder="prod_app")


@app.route("/")
def hello_world():
    return current_app.send_static_file("index.html")


@app.route("/api/login", methods=["POST"])
def login():
    request_data = request.get_json()
    username = request_data["username"]
    password = request_data["password"]
    key = request_data["key"]

    try:
        current_user = controller.get_user(username)
        controller.check_password(current_user, password)
        controller.check_key_exists(key)
        return jsonify("ok!")
    except Exception as e:
        return jsonify(str(e))


@app.route("/api/logout", methods=["POST"])
def logout():
    return jsonify("ok!")


def users():
    """Create user, check users, delete user"""
    pass
