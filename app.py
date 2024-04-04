from flask import Flask, render_template, request
import jinja2
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        result = num1 + num2
        return render_template('index.html', result=result)
@app.route('/66', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        result = num1 + num2
        return render_template('dd.html', result=result)        
   

if __name__ == '__main__':
    app.run(debug=True)
