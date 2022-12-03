#!/usr/bin/python3
"""
Module routes
"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.teardown_appcontext
def teardown(exit):
    """ Closes storage session at the end of endpoint """
    storage.close()

@app.route("/states_lists")
def states_lists():
    """ List states from storage """
    states = storage.all("State")
    return render_template("7-states_list.html", states=states)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
