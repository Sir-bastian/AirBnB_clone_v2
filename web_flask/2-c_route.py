#!/usr/bin/python3
'''
A script that starts a Flask web application:
    -Listens on 0.0.0.0, port 5000
Routes:
    -/: display “Hello HBNB!”
    -/hbnb: display “HBNB”
    -/c/<text>: display “C ” followed by the value of the text variable
    -*(replace underscore _ symbols with a space )
'''
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    return "HelloHBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """replace underscores with spaces"""
    text = text.replace('_', ' ')
    return "C {}".format(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
