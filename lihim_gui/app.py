from re import S
from flask import Flask, current_app, request, jsonify, session, g
from flask.wrappers import Request
from lihim import controller, models
import functools

app = Flask(__name__, static_folder="prod_app")


def login_required(func):
    @functools.wraps(func)
    def secure_point(*args, **kwargs):
        if "username" not in session:
            return jsonify("Please login.")
        return func(*args, **kwargs)

    return secure_point


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
@login_required
def logout():
    try:
        session.pop("username", None)
        session.pop("key", None)
        return jsonify("ok!")
    except Exception as e:
        return jsonify(str(e))


@app.route("/api/users", methods=["GET", "POST"])
def users():
    """Get users list, create a user"""

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


@app.route("/api/groups", methods=["GET", "POST"])
@login_required
def groups():
    """Get groups of current user, create a new group."""
    try:
        current_user = controller.get_user(session["username"])
        if request.method == "GET":
            groups = [group.name for group in controller.check_groups(current_user)]
            return jsonify(groups)
        elif request.method == "POST":
            request_data = request.get_json()
            group_name = request_data["group_name"]
            controller.create_group(group_name, current_user)
            return jsonify("ok!")
    except Exception as e:
        return jsonify(e)


@app.route("/api/groups/<int:id>", methods=["GET", "DELETE"])
def group():
    pass
