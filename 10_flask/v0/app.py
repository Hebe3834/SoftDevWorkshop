# The Nameless Team: Patrick Ging, Eric Guo, Hebe Huang
# SoftDev
# Occupation picker using Flask
# 2021-10-04

from flask import Flask
app = Flask(__name__) # Q0: This looks like a Java constructor

@app.route("/") # Q1: '/' might refer to a root directory
def hello_world():
    print(__name__) # Q2: This prints "__main__" to terminal
    return "No hablo queso!"  # Q3: This will appear on the screen.

app.run()  # Q4: I haven't seen this before
