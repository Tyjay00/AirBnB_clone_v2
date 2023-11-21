#!/usr/bin/python3
"""This script starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'
"""
from flask import Flask  # Import the Flask module

app = Flask(__name__)  # Create an instance of the Flask class


@app.route("/", strict_slashes=False)  # Define the route for the index page
def hello_hbnb():
    """This function is called when the root '/' route of the app is accessed."""
    return "Hello HBNB!"  # Return the string to be displayed on the webpage


if __name__ == "__main__":
    app.run(host="0.0.0.0")  # Run the Flask application
