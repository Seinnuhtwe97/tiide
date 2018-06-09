from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World"

@app.route("/pyae")
def sein():
    return "Hello Sein Nu Htwe"
