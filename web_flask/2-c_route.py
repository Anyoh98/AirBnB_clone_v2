#!/usr/bin/python3
"""
A imple flask web application
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """return the Giveb answer"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """return the given answer"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """
    Displays “C ” followed by the value of the text variable.
    Replaces underscores with spaces in the text.
    """
    return 'C ' + text.replace('_', ' ')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
