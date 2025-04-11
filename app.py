from flask import Flask, render_template
import datetime
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, World!, I\'m flask"


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    now = datetime.datetime.now()
    return render_template('hello.html', name=name, time=now)

@app.route('/today')
def display_today():
    return str(datetime.datetime.now())