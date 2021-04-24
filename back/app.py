import pymongo
from flask_cors import CORS
from bson import ObjectId, json_util
from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)
CORS(app)
# myclient = pymongo.MongoClient("mongodb://localhost:27017")
myclient = pymongo.MongoClient("mongodb+srv://itnews:admin@itnews.ke8gb.mongodb.net")
mydb = myclient["Adv"]
post = mydb["post"]
comm = mydb["comment"]

# ----------------------------CREATE------------------------------------


@app.route("/createpost", methods=["POST"])
def create_post():
    now = datetime.now()
    dt = now.strftime("%d/%m/%Y %H:%M")
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
        "view": 0,
        "vote": [],
        "time": dt,
    }
    x = post.insert_one(newpost)
    return jsonify({"status": "Create Success"})


@app.route("/createcomment", methods=["POST"])
def create_comm():
    now = datetime.now()
    dt = now.strftime("%d/%m/%Y %H:%M")
    newcomm = {
        "user_id": request.json["user_id"],
        "username": request.json["username"],
        "desc": request.json["desc"],
        "post_id": ObjectId(request.json["post_id"]),
        "time": dt,
    }
    x = comm.insert_one(newcomm)
    return jsonify({"status": "Create Success"})


# --------------------------------GET---------------------------------


# @app.route("/allpost", methods=["GET"])
# def get_postall():
#     gpost = []
#     for x in post.find().sort("time", -1):
#         gpost.append(
#             {
#                 "_id": str(x["_id"]),
#                 "newtitle": x["newtitle"],
#                 "newimg": x["newimg"],
#                 "newdes": x["newdes"],
#                 "newurl": x["newurl"],
#                 "posttitle": x["posttitle"],
#                 "newtime": x["newtime"],
#                 "postdes": x["postdes"],
#                 "user_id": x["user_id"],
#                 "username": x["username"],
#                 "view": x["view"],
#                 "vote": x["vote"],
#                 "time": x["time"],
#             }
#         )
#     return jsonify(gpost)


@app.route("/allpost", methods=["GET"])
def get_postall():
    gpost = post.aggregate(
        [
            {
                "$lookup": {
                    "from": "comment",
                    "localField": "_id",
                    "foreignField": "post_id",
                    "as": "comment",
                }
            },
            {
                "$project": {
                    "_id": {"$toString": "$_id"},
                    "newtitle": 1,
                    "newimg": 1,
                    "newdes": 1,
                    "newurl": 1,
                    "posttitle": 1,
                    "newtime": 1,
                    "postdes": 1,
                    "user_id": 1,
                    "username": 1,
                    "view": 1,
                    "vote": 1,
                    "time": 1,
                    "comment._id": 1,
                }
            },
            {"$sort": {"time": -1}},
        ]
    )
    return json_util.dumps(gpost)


# @app.route("/allpost/<page>", methods=["GET"])
# def get_postpage(page):
#     gpost = []
#     if page == "1":
#         for x in post.find().sort("time", -1).limit(2):
#             gpost.append(
#                 {
#                     "_id": str(x["_id"]),
#                     "newtitle": x["newtitle"],
#                     "newimg": x["newimg"],
#                     "newdes": x["newdes"],
#                     "newurl": x["newurl"],
#                     "posttitle": x["posttitle"],
#                     "newtime": x["newtime"],
#                     "postdes": x["postdes"],
#                     "user_id": x["user_id"],
#                     "username": x["username"],
#                     "view": x["view"],
#                     "vote": x["vote"],
#                     "time": x["time"],
#                 }
#             )
#     elif page == "2":
#         for x in post.find().sort("time", -1).limit(4):
#             gpost.append(
#                 {
#                     "_id": str(x["_id"]),
#                     "newtitle": x["newtitle"],
#                     "newimg": x["newimg"],
#                     "newdes": x["newdes"],
#                     "newurl": x["newurl"],
#                     "posttitle": x["posttitle"],
#                     "newtime": x["newtime"],
#                     "postdes": x["postdes"],
#                     "user_id": x["user_id"],
#                     "username": x["username"],
#                     "view": x["view"],
#                     "vote": x["vote"],
#                     "time": x["time"],
#                 }
#             )
#     return jsonify(gpost)


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


# @app.route("/gpost/<id>", methods=["GET"])
# def get_post(id):
#     gpost = {}
#     v = post.find_one_and_update({"_id": ObjectId(id)}, {"$inc": {"view": 1}})
#     for x in post.find({"_id": ObjectId(id)}):
#         gpost = {
#             "_id": str(x["_id"]),
#             "newtitle": x["newtitle"],
#             "newimg": x["newimg"],
#             "newdes": x["newdes"],
#             "newtime": x["newtime"],
#             "newurl": x["newurl"],
#             "posttitle": x["posttitle"],
#             "postdes": x["postdes"],
#             "user_id": x["user_id"],
#             "username": x["username"],
#             "view": x["view"],
#             "vote": x["vote"],
#             "time": x["time"],
#         }
#     return jsonify(gpost)


@app.route("/gpost/<id>", methods=["GET"])
def get_post(id):
    v = post.find_one_and_update({"_id": ObjectId(id)}, {"$inc": {"view": 1}})
    gpost = post.aggregate(
        [
            {
                "$lookup": {
                    "from": "comment",
                    "localField": "_id",
                    "foreignField": "post_id",
                    "as": "comment",
                }
            },
            {
                "$project": {
                    "_id": {"$toString": "$_id"},
                    "newtitle": 1,
                    "newimg": 1,
                    "newdes": 1,
                    "newurl": 1,
                    "posttitle": 1,
                    "newtime": 1,
                    "postdes": 1,
                    "user_id": 1,
                    "username": 1,
                    "view": 1,
                    "vote": 1,
                    "time": 1,
                    "comment._id": 1,
                }
            },
            {"$match": {"_id": id}},
        ]
    )
    return json_util.dumps(gpost)


@app.route("/comment/<id>", methods=["GET"])
def get_comm(id):
    gcomm = []
    for x in comm.find({"post_id": ObjectId(id)}).sort("time", -1):
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
    x = comm.update_many(gcomm, newdata)
    return jsonify({"status": "Update Success"})


# -----------------------------DELETE----------------------------------


@app.route("/delpost/<id>", methods=["DELETE"])
def delete_post(id):
    x = post.delete_one({"_id": ObjectId(id)})
    y = comm.delete_many({"post_id": ObjectId(id)})
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
    # app.run(host="127.0.0.1", port=81)
    app.run(debug=False)