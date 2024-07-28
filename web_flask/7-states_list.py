#!/usr/bin/python3
"""
A minimal app that
routes that routes states list
"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
states = sorted(list(storage.all("State").values()), key=lambda x: x.name)


@app.route('/states_list', strict_slashes=False)
def stateList():
    """
    Function that renders the states list
    """
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
