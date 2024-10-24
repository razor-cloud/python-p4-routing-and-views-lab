#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route("/print/<quote>")
def print_string(quote):
    print(quote)
    return f'{quote}'


@app.route("/count/<int:number>")
def count(number):
    count = f''
    for n in range(number):
        count += f'{n}\n'
    return count


@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == "+":
        result = num1 + num2 
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        return "<h1>Invalid operation</h1>"
    return str(result)


if __name__ == '__main__':
    app.run(port=5555, debug=True)