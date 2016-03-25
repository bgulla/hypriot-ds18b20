#!/usr/bin/python
from flask import Flask, jsonify
from flask.ext.cors import CORS
import ds18b20

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/rest/api/v1.0/temperature', methods=['GET'])
def get_tasks():
    return jsonify({'sensors': ds18b20.get_readings()})

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8080)
