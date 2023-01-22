#!/usr/bin/python3
"""Flask"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
        """hello_route"""
            return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
        """hbnb"""
            return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
        """c_route"""
            return "C {}".format(text.replace("_", " "))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text="is cool"):
        """python_route"""
            return "Python {}".format(text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
        """number_route"""
            if isinstance(n, int):
                        return "{} is a number".format(n)


if __name__ == "__main__":
        app.run()
