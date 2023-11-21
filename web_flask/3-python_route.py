#!/usr/bin/python3
"""This script starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'.
    /hbnb: Displays 'HBNB'.
    /c/<text>: Displays 'C' followed by the value of <text>.
    /python/(<text>): Displays 'Python' followed by the value of <text>.
"""
from flask import Flask  # Import the Flask module

app = Flask(__name__)  # Create an instance of the Flask class


@app.route("/", strict_slashes=False)  # Define the route for the index page
def hello_hbnb():
    """This function is called when the root '/' route of the app is accessed."""
    return "Hello HBNB!"  # Return the string to be displayed on the webpage


@app.route("/hbnb", strict_slashes=False)  # Define the route for the '/hbnb' page
def hbnb():
    """This function is called when the '/hbnb' route of the app is accessed."""
    return "HBNB"  # Return the string to be displayed on the webpage


@app.route("/c/<text>", strict_slashes=False)  # Define the route for the '/c/<text>' page
def c(text):
    """This function is called when the '/c/<text>' route of the app is accessed.

    Args:
        text (str): The text to be displayed after 'C '
    """
    text = text.replace("_", " ")  # Replace underscores in the text with spaces
    return "C {}".format(text)  # Return the string 'C ' followed by the text


@app.route("/python", strict_slashes=False)  # Define the route for the '/python' page
@app.route("/python/<text>", strict_slashes=False)  # Define the route for the '/python/<text>' page
def python(text="is cool"):
    """This function is called when the '/python' or '/python/<text>' route of the app is accessed.

    Args:
        text (str): The text to be displayed after 'Python ', defaults to 'is cool'
    """
    text = text.replace("_", " ")  # Replace underscores in the text with spaces
    return "Python {}".format(text)  # Return the string 'Python ' followed by the text


if __name__ == "__main__":
    app.run(host="0.0.0.0")  # Run the Flask application
