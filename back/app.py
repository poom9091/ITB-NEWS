import pymongo
from flask_cors import CORS
from bson import json_util
from flask import Flask, jsonify, request

app = Flask(__name__)
CORS(app)
myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient["Adv"]
post = mydb["post"]


@app.route("/", methods=["POST"])
def Create_post():
    newpost = {
        "newtitle": request.json["newtitle"],
        "newimg": request.json["newimg"],
        "newdes": request.json["newdes"],
        "newurl": request.json["newurl"],
        "newtime": request.json["newtime"],
        "posttitle": request.json["posttitle"],
        "postdes": request.json["postdes"],
    }
    x = post.insert_one(newpost)
    return jsonify({"status": "Create Success"})


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=81)