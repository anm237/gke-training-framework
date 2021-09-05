from flask import Flask
import os

app = Flask(__name__)

@app.route("/akash")
def hello():
    return "Hello Akash"


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=5000)
