#!/usr/bin/python3
"""
The flask web applictaion
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """returns the given answer"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Return the guven answzer"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """
    Displays “C ” followed by the value of the text variable.
    Replaces underscores with spaces in the text.
    """
    return 'C ' + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythoniscool(text='is cool'):
    """Dsiplya python and the name of teh variable"""
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def imanumber(n):
    """Display n only if the n is an intege"""
    return "{:d} is a number".format(n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
