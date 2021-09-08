from .app import app
from flask import session
import argparse
import webbrowser
import os


def start():
    parser = argparse.ArgumentParser()
    parser.add_argument("-dev", "--develop", action="store_true")
    args = parser.parse_args()

    if args.develop:
        app_key = generate_app_key()
        app.secret_key = app_key
        app.run(debug=True)
    else:
        app_key = generate_app_key()
        app.secret_key = app_key
        webbrowser.open_new("localhost:5000")
        app.run()


def generate_app_key() -> bytes:
    return os.urandom(16)
