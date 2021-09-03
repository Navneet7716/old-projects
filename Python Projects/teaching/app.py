from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/hello", methods=["GET"])
def home():

    return render_template("hello.html")
