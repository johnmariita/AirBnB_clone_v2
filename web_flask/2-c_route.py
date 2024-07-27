#!/usr/bin/python3
"""
minimal web app that listens on 0.0.0.0, port 5000
"""


from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """
    returns Hello HBNB!
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    returns HBNB
    """
    return 'HBNB'


@app.route('/c/<text>')
def cFun(text):
    """
    Function that checks the route
    after c and returns a string
    """
    text = text.replace('_', ' ')
    return "C " + text


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
