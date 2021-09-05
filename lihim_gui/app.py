from flask import Flask, current_app

app = Flask(__name__, static_folder="prod_app")


@app.route("/")
def hello_world():
    return current_app.send_static_file("index.html")
