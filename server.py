from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
app.secret_key = 'dee892ad02ebb1ab49cac878698a8eb3'


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html')


app.run(debug=True)
