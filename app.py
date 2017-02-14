from flask import Flask, request, redirect, render_template, url_for
from models import *

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
@app.route('/request-counter', methods = ['GET', 'POST'])
def counter():
    if request.method == 'GET':
        Request.create(type= 'get')
        return render_template("index.html")

    elif request.method == 'POST':
        Request.create(type= 'post')
        return render_template("index.html")


@app.route('/statistics', methods=['GET', 'POST'])
def statistics():
    query = Request.select()
    return render_template("stats.html", query=query)


#@app.route('/json-generator')















app.run(debug=True, port=5000, host='0.0.0.0')