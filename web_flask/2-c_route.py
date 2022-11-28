#!/usr/bin/python3
""" Module 1-hbnb_route """

from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>")
def c(text):
    return "C {}".format(escape(text.replace("_", " ")))


if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0")
