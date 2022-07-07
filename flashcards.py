from flask import Flask
from datetime import datetime

app = Flask(__name__)


@app.route("/")  # a view function (decorator). We are decorating our welcome function
def welcome():
    return "Welcome to my Flash Card application!"


@app.route("/date")  # a view function (decorator). We are decorating our welcome function.
def date():
    return "cev" + str(datetime.now())


if __name__ == "__main__":
    app.run()
