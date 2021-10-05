# The Nameless Team: Patrick Ging, Eric Guo, Hebe Huang
# SoftDev
# Occupation picker using Flask
# 2021-10-04

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    return "No hablo queso!" # returns to site at 127.0.0.1:5000

app.run()
