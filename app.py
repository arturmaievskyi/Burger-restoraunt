from flask import Flask, render_template

app = Flask()

@app.route("/")
def index():
    return render_template("index.html", title = "Burger restorant")
@app.route("/burgers")
def burgers():
    return render_template("burger.html")
@app.route("/menus")
def menu():
    