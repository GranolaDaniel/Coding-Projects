from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def board():
    return render_template('board.html')
