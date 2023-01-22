#!/usr/bin/python3
"""
script starts a Flask web application
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
        """returns Hello HBNB!"""
            return 'Hello HBNB!'


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
        """display "C " followed by the value of the text variable"""
            return 'C ' + text.replace('_', ' ')


@app.route('/python/', strict_slashes=False, defaults={'text': 'is cool'})
@app.route('/python/<text>', strict_slashes=False)
def index_python(text):
        """display "python " followed by the value of the text variable"""
            text = text.replace("_", " ")
                return "Python {}".format(text)


if __name__ == '__main__':
        app.run(host='0.0.0.0', port='5000')
