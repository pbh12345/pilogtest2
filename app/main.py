from flask import Flask,request, jsonify
app = Flask(__name__)
app.config["DEBUG"] = True


@app.route("/", methods=["GET"])
def home():
    out = {"msg": "welcome"}
    return jsonify(out)


@app.route("/tripler", methods= ["GET"])
def hello():
    id = int(request.args["id"])
    out = {
        "Result" : 3*id
    }
    return jsonify(out)


#