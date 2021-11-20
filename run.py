import os
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    # __main__ is the name of the default module in Python
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
# DO NOT PUT debug=True IN LIVE PROJECT, CHANGE TO
# debug=False FOR SECURITY REASONS
# debug = True allows for arbitrary code to be run which is a security flaw
