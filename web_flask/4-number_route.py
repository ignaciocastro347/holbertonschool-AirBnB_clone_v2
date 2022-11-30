#!/usr/bin/python3
""" Module routes """

from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def index():
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    return "HBNB"


@app.route("/c/<text>")
def c(text):
    return "C {}".format(text.replace("_", " "))


@app.route("/python")
@app.route("/python/<text>")
def python_route(text="is cool"):
    return "Python {}".format(text.replace("_", " "))


@app.route("number/<int:n>")
def number(n):
    return n + " is a number"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
