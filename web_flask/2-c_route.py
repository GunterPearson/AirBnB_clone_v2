#!/usr/bin/python3
""" 2-c_route """
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ for basic / """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ for /hbnb """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def string_var(text):
    """ return text """
    return "C {}".format(text.replace("_", " "))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
