from flask import Flask, request, redirect, render_template, url_for
import models

app = Flask(__name__)

@app.route('/request-counter', methods = ['GET', 'POST'])
def counter():
    if request.method == 'GET':
        Request.create(type= 'get')
    elif request.method == 'POST':
        Request.create(type= 'post')

@app.route('/statistics', methods=['GET', 'POST'])
def statistics:
    query = Request.select()
    return


@app.route('/json-generator')















app.run(debug=True, port=5000, host='0.0.0.0')