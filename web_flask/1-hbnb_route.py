#!/usr/bin/python3
'''
A script that starts a Flask web application
    It listens on 0.0.0.0, port 5000
    Routes:
        - /: display "Hello HBNB!"
        -/hbnb: display "HBNB"
Must use the option strict_slashes=False in route definition
'''
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    return "HelloHBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
