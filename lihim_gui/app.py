from flask import Flask, current_app, request, jsonify, session
from lihim import controller, models

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
        session["username"] = username
        session["key"] = key
        return jsonify("ok!")
    except Exception as e:
        return jsonify(str(e))


@app.route("/api/logout", methods=["POST"])
def logout():
    try:
        session.pop("username", None)
        session.pop("key", None)
        return jsonify("ok!")
    except Exception as e:
        return jsonify(str(e))


@app.route("/api/users", methods=["GET", "POST"])
def users():
    """Check users, create a user"""

    try:
        if request.method == "GET":
            users = [user.username for user in controller.check_users()]
            return jsonify(users)
        elif request.method == "POST":
            request_data = request.get_json()
            username = request_data["username"]
            password = request_data["password"]
            key_path = request_data["key_path"]
            key_name = request_data["key_name"]

            key = models.create_key(key_path, key_name, username)
            controller.create_user(username, password, key)

            return jsonify("ok!")
    except Exception as e:
        return jsonify(str(e))


def groups():
    # "username" in session
    pass
