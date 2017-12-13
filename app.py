"""
Main module app.py
"""

from flask import Flask


app = Flask(__name__)

@app.route('/')
def welcome():
    """
    Returns Welcome
    """
    return 'Welcome'
