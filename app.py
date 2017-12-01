from flask import Flask, make_response, request, jsonify, json
from flask import render_template, Markup, abort


app=Flask(__name__)

@app.route('/')
def welcome():
    return 'Welcome'
