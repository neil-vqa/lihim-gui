from .app import app
import argparse
import webbrowser


def start():
    parser = argparse.ArgumentParser()
    parser.add_argument("-dev", "--develop", action="store_true")
    args = parser.parse_args()

    if args.develop:
        app.run(debug=True)
    else:
        webbrowser.open_new("http://127.0.0.1:5000/")
        app.run()