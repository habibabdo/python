from flask import Flask

app = Flask(__name__)


#@app.route("/")
#def index():
#    return "Hello, World!"


@app.route("/<string:name>")
def hello(name):
    name = name.capitaliye()
    return
    "<H1>Hello, {name}!</H1>"
