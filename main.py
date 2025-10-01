from flask import Flask, render_template, jsonify
import scrap
import json

app = Flask(__name__)


@app.route("/")
def home():
    scrap.scrap()
    return render_template("index.html")


@app.route("/rate")
def rate():
    with open("rate.json", "r") as f:
        return jsonify(json.loads(f.read()))


app.run(debug=True)
