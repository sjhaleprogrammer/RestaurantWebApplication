from flask import Flask, render_template
app = Flask(__name__, template_folder= "live-dinner")

@app.route("/")
def hello():
    return render_template("menu.html")
