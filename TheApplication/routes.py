from __main__ import app
from flask import url_for, render_template, request, redirect

@app.route('/')
def home():
    return render_template("home.html")