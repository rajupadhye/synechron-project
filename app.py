import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Hello and Welcome to Thinknyx app!"

@app.route('/learningjenkins')
def hello():
    return "We found few issues with Ubuntu for Jenkins in our lab!"

if __name__=="__main__":
    app.run(host="0.0.0.0", port=8080)
