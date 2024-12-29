from flask import Flask
from flask import request
from flask import redirect

app = Flask(__name__)


@app.route("/")
def home():
    html = ""
    with open("index.html", "r", encoding="utf-8") as f:
        html = f.read()
    return html


@app.route("/search")
def search():
    html = ""
    with open("search.html", "r", encoding="utf-8") as f:
        html = f.read()
    return html


@app.route("/search_car", methods=["POST"])
def search_car():
    html = ""
    car = request.form.get("car")
    money = ""
    with open("search.html", "r", encoding="utf-8") as f:
        html = f.read()
    try:
        with open(f"cars/{car}.txt", "r", encoding="utf-8") as f:
            money = f.read()
    except:
        return html.replace("<out/>", "無此車輛")
    return html.replace("<out/>", f"{money}元")


app.run(debug=True, host="0.0.0.0")
