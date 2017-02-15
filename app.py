from flask import Flask, request, redirect, render_template, url_for
from models import *

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def homepage():
    return render_template('index.html')

@app.route('/request-counter', methods = ['GET', 'POST'])
def counter():
    if request.method == 'GET':
        Request.create(type= 'get')
        return redirect(url_for('homepage'))

    elif request.method == 'POST':
        Request.create(type= 'post')
        return redirect(url_for('homepage'))


@app.route('/statistics', methods=['GET', 'POST'])
def statistics():
    query = Request.select()
    return render_template("stats.html", query=query)


@app.route('/json-generator', methods = ["GET", "POST"])
def json_generator():
	params = request.args.items()
	for item in params:
		print(item)
	return redirect(url_for('counter'))















app.run(debug=True, port=5000, host='0.0.0.0')