from flask import Flask, request, render_template_string,render_template
from jinja2 import Environment, escape
from itsdangerous import json


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
   
     
    return render_template('index.html',e=e)

if __name__ == '__main__':
    app.run(debug=true)
