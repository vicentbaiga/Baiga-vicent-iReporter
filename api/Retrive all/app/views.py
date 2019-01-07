from flask import Flask
from flask import request, jsonify
import datetime
from app.models import Red_flag, redflag

app = Flask(__name__)


@app.route('/api/v1/red-flags', methods=['POST'])
def post_redflag():
    data = request.get_json()
    created_by = data['created_by'] 
    created_on = datetime.datetime.now()
    location = data['location']  
    comment = data['comment']


    record = Red_flag(created_by,created_on,location,comment)
    redflag.append(record)

    return jsonify({"message":"redflag successfully created"})

@app.route('/api/v1/red-flags/<int:id>', methods=['DELETE'])
def delete_redflag(id):
    for i in redflag:
        if i.__dict__['id'] == id:
            redflag.remove(redflag[0])
        return jsonify({"message": "redflag deleted successfully"})

@app.route('/api/v1/red-flags/<int:id>', methods=['GET'])
def get_redflag_by_id(id):
    for i in redflag:
        if i.__dict__['id'] == id:
            return jsonify({"red-flag":i.__dict__})
        
    return jsonify({"message":"redflag not found"})

@app.route('/api/v1/red-flags', methods=['GET'])
def get_all_redflags():
    display_redflag = []
    for i in redflag:
        display_redflag.append(i.__dict__)
    return jsonify({"message":display_redflag})
