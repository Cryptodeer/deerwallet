from flask import Flask, render_template, request, url_for, jsonify
import deersrv
import json

application = Flask(__name__)

@application.route("/deerwallet/v2", methods=["POST"])
def deerwalletpost():
	return jsonify(deersrv.proc(json.loads(request.data)))

@app.errorhandler(404)
def page_not_found(e):
    return jsonify(deersrv.Error('INVALID_REQUEST_TYPE').get()), 404

if __name__ == "__main__":
    application.run(host='127.0.0.1')