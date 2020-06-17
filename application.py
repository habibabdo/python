from flask import  Flask

app=Flask(__name__)

@app.route("/")
def index():
    return "Hello, World!"


@app.route("/Habib")
def Habib():
    return "Hello, Habib!"


@app.route("/Abdo")
def Abdo():
    return "Hello, Abdo!"
