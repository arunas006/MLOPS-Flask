from flask import Flask,request,jsonify

app=Flask(__name__)

@app.route("/ping")
def sample():
    return "ARUN'S FRIST FLASK TRY"

