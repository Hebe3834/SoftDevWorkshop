# The Brave Hamsters: Justin Zou, Hebe Huang
# SoftDev
# K19: A RESTful Journey Skyward
# 2021-11-23

from flask import Flask, render_template
import urllib.request
import json

app = Flask(__name__)

@app.route("/")
def home():
    api_key = open('key_nasa.txt', 'r').read()
    nasa = urllib.request.urlopen('https://api.nasa.gov/planetary/apod?api_key=' + api_key)
    d = json.loads(nasa.read()) #json.loads converts the string from nasa.read() into a dictionary
    return render_template("main.html", pic = d["url"], explanation = d["explanation"])


if __name__ == "__main__":
    app.debug = True
    app.run()
