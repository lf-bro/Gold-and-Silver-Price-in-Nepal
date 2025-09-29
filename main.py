from flask import Flask, render_template
import scrap

app = Flask(__name__)


@app.route("/")
def home():
    scrap.scrap()
    return render_template("index.html")


@app.route("/rate")
def rate():
    return "ok"


app.run(debug=True)
