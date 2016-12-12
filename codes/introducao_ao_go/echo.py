#!/usr/bin/python3
from flask import Flask, jsonify
app = Flask(__name__)


@app.route("/api/")
def api():
    return jsonify({"apple": 5, "lettuce": 7})

if __name__ == "__main__":
    app.run()
