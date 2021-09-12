from flask import Flask, current_app, request, jsonify, session
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
    request_data = request.json
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
            request_data = request.json
            username = request_data["username"]
            password = request_data["password"]
            key_path = request_data["key_path"]
            key_name = request_data["key_name"]

            key = models.create_key(key_path, key_name, username)
            controller.create_user(username, password, key)

            return jsonify("ok!")
    except Exception as e:
        return jsonify(str(e))


@app.route("/api/groups/", methods=["GET", "POST"])
@login_required
def groups():
    """Get groups of current user, create a new group."""
    try:
        current_user = controller.get_user(session["username"])
        if request.method == "GET":
            groups = [
                {"name": group.name, "id": group.id}
                for group in controller.check_groups(current_user)
            ]
            return jsonify(groups)
        elif request.method == "POST":
            request_data = request.json
            group_name = request_data["group_name"]
            controller.create_group(group_name, current_user)
            return jsonify("ok!")
    except Exception as e:
        return jsonify(str(e))


@app.route("/api/groups/<int:id>", methods=["GET", "DELETE"])
@login_required
def group(id):
    """
    Get certain group to show its key-value pairs,
    delete the group.
    """
    try:
        current_user = controller.get_user(session["username"])
        group_name = request.args["group_name"]
        if request.method == "GET":
            pairs = [
                {"key": pair.key_string, "id": pair.id, "group_id": pair.group_id}
                for pair in controller.check_group_pairs(group_name, current_user)
            ]
            return jsonify(pairs)
        elif request.method == "DELETE":
            controller.delete_group(group_name, current_user)
            return jsonify("ok!")
    except Exception as e:
        return jsonify(str(e))


@app.route("/api/pairs/", methods=["POST"])
@login_required
def pairs():
    # key: str, value: str, group: str, current_user: User
    try:
        if request.method == "POST":
            pass
    except Exception as e:
        return jsonify(str(e))


@app.route("/api/pairs/<int:id>", methods=["GET", "DELETE"])
@login_required
def pair(id):
    try:
        current_user = controller.get_user(session["username"])
        group_name = request.args["group_name"]
        key_string = request.args["key_string"]
        if request.method == "GET":
            key_file = session["key"]

            pair = controller.load_pair_in_group(group_name, key_string, current_user)
            value_string = controller.use_key(key_file, decrypt_text=pair.value_string)
            return jsonify(value_string)
        elif request.method == "DELETE":
            pass
    except Exception as e:
        return jsonify(str(e))
