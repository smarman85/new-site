from flask import Flask, flash, redirect, render_template, request, session, abort, jsonify, Response

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World"

@app.route("/health", methods = ['GET'])
def healthcheck():
    data = {
            'healthy' : True
            }
    resp = jsonify(data)
    resp.status_code = 200
    resp.headers['Link'] = 'https://gasthaus.marqeta.com'
    return resp

@app.errorhandler(500)
def page_not_found(error):
    return render_template('error.html')

@app.errorhandler(404)
def pageNotFound(error):
    return "page not found"

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False)
