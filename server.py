from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('./index.html')


@app.route('/contact')
def welcome():
    return render_template('./contact.html')


@app.route('/about')
def some():
    return render_template('./about.html')


