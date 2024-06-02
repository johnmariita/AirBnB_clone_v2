#!/usr/bin/python3
"""
A minimal application using flask
"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """
    Function that returns the message hello HBNB! to the browser
    """
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
