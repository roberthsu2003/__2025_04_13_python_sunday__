from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<H1>Hello, 世界!</H1>"