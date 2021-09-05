from flask import Flask

app = Flask(__name__, template_folder="templates", static_folder="static")


@app.route("/")
def hello_world():
    return "hi"


if __name__ == "__main__":
    app.run(debug=True)
