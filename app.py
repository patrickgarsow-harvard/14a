from flask import Flask
import datetime

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World! Welcome to S14A2023</p>"

@app.route("/datetime")
def datetime_out():
    servCurrentTime = datetime.now()
    servUTCDatetime = datetime.now(timezone.utc)
    return "<p>Server Date/Time: {servCurrentTime}</p> <p>Server UTC Date/Time: {servUTCDatetime}</p> <p>Owner's Date/Time: {servCurrentTime}</p>"