import pymongo
from flask_cors import CORS
from bson import json_util
from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)
CORS(app)
myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient["Adv"]
post = mydb["post"]
comm = mydb["comment"]
user = mydb["user"]


@app.route("/loginfb", methods=["POST"])
def fb_login():
    return


@app.route("/logingg", methods=["POST"])
def gg_login():
    return


@app.route("/createpost", methods=["POST"])
def create_post():
    now = datetime.now()
    dt = now.strftime("%d/%m/%Y %H:%M:%S")
    newpost = {
        "newtitle": request.json["newtitle"],
        "newimg": request.json["newimg"],
        "newdes": request.json["newdes"],
        "newurl": request.json["newurl"],
        "newtime": request.json["newtime"],
        "posttitle": request.json["posttitle"],
        "postdes": request.json["postdes"],
        "user_id": request.json["user_id"],
        "username": request.json["username"],
        "view": "0",
        "vote": "0",
        "time": dt,
    }
    x = post.insert_one(newpost)
    return jsonify({"status": "Create Success"})


@app.route("/createcomment", methods=["POST"])
def create_comm():
    now = datetime.now()
    dt = now.strftime("%d/%m/%Y %H:%M:%S")
    newcomm = {
        "user_id": request.json["user_id"],
        "username": request.json["username"],
        "desc": request.json["desc"],
        "post_id": request.json["post_id"],
        "time": dt,
    }
    x = comm.insert_one(newcomm)
    return jsonify({"status": "Create Success"})


@app.route("/post", methods=["GET"])
def get_postall():
    gpost = []
    for x in post.find():
        gpost.append(
            {
                "_id": str(x["_id"]),
                "newtitle": x["newtitle"],
                "newimg": x["newimg"],
                "newdes": x["newdes"],
                "posttitle": x["posttitle"],
                "postdes": x["postdes"],
                "user_id": x["user_id"],
                "username": x["username"],
                "view": x["view"],
                "vote": x["vote"],
                "time": x["time"],
            }
        )
    return jsonify(gpost)


@app.route("/post/<id>", methods=["GET"])
def get_post(id):
    gpost = []
    for x in post.find({"_id": id}):
        gpost.append(
            {
                "newtitle": x["newtitle"],
                "newimg": x["newimg"],
                "newdes": x["newdes"],
                "posttitle": x["posttitle"],
                "postdes": x["postdes"],
                "username": x["username"],
                "view": x["view"],
                "vote": x["vote"],
                "time": x["time"],
            }
        )
    return jsonify(gpost)


@app.route("/comment/<id>", methods=["GET"])
def get_comm(id):
    gcomm = []
    for x in comm.find({"post_id": id}):
        gcomm.append(
            {
                "desc": x["desc"],
                "username": x["username"],
                "time": x["time"],
            }
        )
    return jsonify(gcomm)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=81)