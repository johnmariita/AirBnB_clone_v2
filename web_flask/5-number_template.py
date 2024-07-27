#!/usr/bin/python3
"""
minimal web app that listens on 0.0.0.0, port 5000
"""


from flask import Flask, render_template
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


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text="is cool"):
    """
    Function that checks the route
    after python and returns a string
    """
    text = text.replace('_', ' ')
    return "Python " + text


@app.route('/number/<int:n>', strict_slashes=False)
def num(n):
    """
    Function that checks if
    a route contains a number or not
    """
    return f"{n} is a number"


@app.route('/number_template/<int:n>')
def num_temp(n):
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
