from flask import  Flask ,render_template

app=Flask(__name__)

@app.route("/")
def index():
    headline='Hellow World !'
    return  render_template('index.html',headline=headline)

