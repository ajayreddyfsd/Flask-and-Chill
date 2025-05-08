from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
def func():
    return render_template('./index.html')


# route parameters
# extracts the params from URL and displays accordingly
@app.route('/<varx>/<int:id>')
def hello_world(varx=None, id=None):
    return render_template('./index.html', varx=varx, id=id)


@app.route('/contact')
def welcome():
    return render_template('./contact.html')


@app.route('/about')
def some():
    return render_template('./about.html')


