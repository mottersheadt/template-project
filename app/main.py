from flask import Flask, jsonify, request
from flask_cors import CORS
from app.src import business

app = Flask(__name__)

# enable CORS
CORS(app, resources={'/*': {'origins': '*'}})

@app.route('/companies', methods=['GET'])
def get_companies():
  return jsonify(business.companies)

@app.route('/submit', methods=['POST', 'GET'])
def submit_data():
  name = request.args.get('name')
  count = business.submit(request.args)
  return jsonify({
    "count": count,
    "name": name
  })
