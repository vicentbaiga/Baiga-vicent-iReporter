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

    return jsonify({"message":"RedFlad has been successfully created"})

