from flask import Flask, Response, request, jsonify
from io import BytesIO
import base64
from flask_cors import CORS, cross_origin
import os
import sys

app = Flask(__name__)
cors = CORS(app)


@app.route("/image", methods=['GET', 'POST'])
def image():
    if(request.method == "POST"):
        bytesOfImage = request.get_data()
        save_path = "picture/image.jpeg"
        with open(save_path, 'wb') as out:
            out.write(bytesOfImage)
        return "Image read"

if __name__=="__main__":
    app.run(host="192.168.45.70",port="19000")

