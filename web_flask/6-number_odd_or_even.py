#!/usr/bin/python3
"""
Module routes
"""
from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def index():
    """ index endpoint """
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """ hbnb endpoint"""
    return "HBNB"


@app.route("/c/<text>")
def c(text):
    """ x endpoint """
    return "C {}".format(text.replace("_", " "))


@app.route("/python")
@app.route("/python/<text>")
def python_route(text="is cool"):
    """ python endpoint """
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>")
def number_route(n):
    """ number endpoint """
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>")
def number_template_hbnb(n):
    """ number endpoint """
    return render_template("5-number.html", number=n)


@app.route("/number_odd_or_even/<int:n>")
def number_odd_or_even(n):
    """ number odd or even endpoint """
    type_number = "even" if n % 2 == 0 else "odd"
    return render_template("6-number_odd_or_even.html",
                           number=n,
                           type_number=type_number)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
