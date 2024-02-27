#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return f"<h1>Python Operations with Flask Routing and Views</h1>"

@app.route("/print/<parameter>")
def print_string(parameter):
    print(parameter)
    return parameter

@app.route('/count/<int:num>')
def count(num):
    res = ""
    for i in range(num):
        res+= str(i) + "\n"
    return res

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    if operation=='+':
        result=num1+num2
    elif operation=='-':
        result=num1-num2
    elif operation=='*':
        result=num1*num2
    elif operation=='div':
        result=num1/num2
    elif operation=='%':
        result=num1%num2
    else:
        result="invalid operation"
    return str(result)


if __name__ == '__main__':
    app.run(port=5555, debug=True)
