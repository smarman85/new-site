from flask import Flask, flash, redirect, render_template, request, session, abort, jsonify, Response

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World"

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False)
