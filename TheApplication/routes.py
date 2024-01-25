# import the app file
from __main__ import app
# import the flask functions
from flask import url_for, render_template, request, redirect

# the routes
@app.route('/')

# home page routes
def home():
    return render_template("home.html")

