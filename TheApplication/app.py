# importing flask
from flask import Flask, render_template

# createing the app
app = Flask(__name__)

# importing the routes file
import routes

# running the app
if __name__ == "__main__":
    app.run(debug=True)


