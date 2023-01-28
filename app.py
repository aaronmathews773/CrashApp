#!/usr/bin/env python3

from flask import Flask, render_template, jsonify, Response, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/postRequest", methods = ["POST"])

@app.route("/getRequest", methods = ["GET"])

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False, threaded=True)
