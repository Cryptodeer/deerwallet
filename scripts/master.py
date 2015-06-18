from flask import Flask, render_template, request, url_for, jsonify
import deersrv
import json

application = Flask(__name__)

@application.route("/deerwallet", methods=["POST"])
def deerwalletpost():
	return jsonify(deersrv.proc(json.loads(request.data)))

if __name__ == "__main__":
    application.run(host='127.0.0.1')