import pymongo
from flask_cors import CORS
from bson import ObjectId
from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)
CORS(app)
myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient["Adv"]
post = mydb["post"]
comm = mydb["comment"]

# ----------------------------CREATE------------------------------------


@app.route("/createpost", methods=["POST"])
def create_post():
    now = datetime.now()
    dt = now.strftime("%H:%M %d/%m/%Y")
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
        "vote": [],
        "time": dt,
    }
    x = post.insert_one(newpost)
    return jsonify({"status": "Create Success"})


@app.route("/createcomment", methods=["POST"])
def create_comm():
    now = datetime.now()
    dt = now.strftime("%H:%M %d/%m/%Y")
    newcomm = {
        "user_id": request.json["user_id"],
        "username": request.json["username"],
        "desc": request.json["desc"],
        "post_id": request.json["post_id"],
        "time": dt,
    }
    x = comm.insert_one(newcomm)
    return jsonify({"status": "Create Success"})


# --------------------------------GET---------------------------------


@app.route("/allpost", methods=["GET"])
def get_postall():
    gpost = []
    for x in post.find().sort("time", -1):
        gpost.append(
            {
                "_id": str(x["_id"]),
                "newtitle": x["newtitle"],
                "newimg": x["newimg"],
                "newdes": x["newdes"],
                "newurl": x["newurl"],
                "posttitle": x["posttitle"],
                "newtime": x["newtime"],
                "postdes": x["postdes"],
                "user_id": x["user_id"],
                "username": x["username"],
                "view": x["view"],
                "vote": x["vote"],
                "time": x["time"],
            }
        )
    return jsonify(gpost)


# @app.route("/post/<name>", methods=["GET"])
# def get_someall(name):
#     gpost = []
#     for x in post.find({"newtitle": name}).sort("time", -1):
#         gpost.append(
#             {
#                 "_id": str(x["_id"]),
#                 "newtitle": x["newtitle"],
#                 "newimg": x["newimg"],
#                 "newdes": x["newdes"],
#                 "newtime": x["newtime"],
#                 "newurl": x["newurl"],
#                 "posttitle": x["posttitle"],
#                 "postdes": x["postdes"],
#                 "user_id": x["user_id"],
#                 "username": x["username"],
#                 "view": x["view"],
#                 "vote": x["vote"],
#                 "time": x["time"],
#             }
#         )
#     return jsonify(gpost)


@app.route("/gpost/<id>", methods=["GET"])
def get_post(id):
    gpost = {}
    for x in post.find({"_id": ObjectId(id)}):
        gpost = {
            "_id": str(x["_id"]),
            "newtitle": x["newtitle"],
            "newimg": x["newimg"],
            "newdes": x["newdes"],
            "newtime": x["newtime"],
            "newurl": x["newurl"],
            "posttitle": x["posttitle"],
            "postdes": x["postdes"],
            "user_id": x["user_id"],
            "username": x["username"],
            "view": x["view"],
            "vote": x["vote"],
            "time": x["time"],
        }
    return jsonify(gpost)


@app.route("/comment/<id>", methods=["GET"])
def get_comm(id):
    gcomm = []
    for x in comm.find({"post_id": id}).sort("time", -1):
        gcomm.append(
            {
                "_id": str(x["_id"]),
                "desc": x["desc"],
                "username": x["username"],
                "time": x["time"],
                "user_id": x["user_id"],
            }
        )
    return jsonify(gcomm)


# -----------------------------UPDATE----------------------------------


@app.route("/editpost/<id>", methods=["PUT"])
def update_post(id):
    gpost = {"_id": ObjectId(id)}
    newdata = {
        "$set": {
            "newtitle": request.json["newtitle"],
            "newimg": request.json["newimg"],
            "newdes": request.json["newdes"],
            "newurl": request.json["newurl"],
            "newtime": request.json["newtime"],
            "posttitle": request.json["posttitle"],
            "postdes": request.json["postdes"],
            "user_id": request.json["user_id"],
            "username": request.json["username"],
            "view": request.json["view"],
            "vote": request.json["vote"],
            "time": request.json["time"],
        }
    }
    x = post.update_many(gpost, newdata)
    return jsonify(newdata)


@app.route("/editcomment/<id>", methods=["PUT"])
def update_comm(id):
    gcomm = {"_id": ObjectId(id)}
    newdata = {
        "$set": {
            "desc": request.json["desc"],
            "time": request.json["time"],
            "user_id": request.json["user_id"],
            "username": request.json["username"],
        }
    }
    x = comm.update_one(gcomm, newdata)
    return jsonify({"status": "Update Success"})


# -----------------------------DELETE----------------------------------


@app.route("/delpost/<id>", methods=["DELETE"])
def delete_post(id):
    gpost = {"_id": ObjectId(id)}
    x = post.delete_one(gpost)
    return jsonify({"status": "Delete success"})


@app.route("/delcomment/<id>", methods=["DELETE"])
def delete_comm(id):
    gcomm = {"_id": ObjectId(id)}
    x = comm.delete_one(gcomm)
    return jsonify({"status": "Delete success"})


# # ------------------------------VOTE-------------------------------------
# @app.route("/vote/<id>", methods=["PUT"])
# def keepvote(id):
#     gpost = {"_id": ObjectId(id)}
#     user_id = request.json["user_id"]
#     vote = {
#         "$push": {
#             "vote": request.json["user_id"],
#         }
#     }
#     x = post.update_one(gpost, vote)
#     return jsonify({"status": "vote Success"})


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=81)