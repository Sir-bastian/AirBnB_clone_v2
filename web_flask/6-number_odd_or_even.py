#!/usr/bin/python3
'''
A script that starts a Flask web application:
    -Listens on 0.0.0.0, port 5000
Routes:
    -/: display “Hello HBNB!”
    -/hbnb: display “HBNB”
    -/c/<text>: display “C ” followed by the value of the text variable
     (replace underscore _ symbols with a space )
    -/python/<text>: Displays "Python", followed by the value of the text
      variable (replace underscore _ symbols with a space)
      the default value of text is "is cool"
    - /number/<n>: display "n is a number" only if n is an integer.
    -/number_template/<n>: display a HTML page only if n is an integer:
        H1 tag: “Number: n” inside the tag BODY
    /number_odd_or_even/<n>: display a HTML page only if n is an integer:
        H1 tag: “Number: n is even|odd” inside the tag BODY
'''
from flask import Flask, render_template

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


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def py(text):
    '''replace underscores with space'''
    text = text.replace('_', ' ')
    return "Python {}".format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    '''The number page'''
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    '''The number_template page'''
    ctxt = {
            'n': n
    }
    return render_template('5-number.html', **ctxt)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even(n):
    '''The odd or even pages'''
    ctxt = {
            'n': n
    }
    return render_template('6-number_odd_or_even.html', **ctxt)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
