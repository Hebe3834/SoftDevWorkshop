# The Nameless Team: Patrick Ging, Eric Guo, Hebe Huang
# SoftDev
# Occupation picker using Flask
# 2021-10-04

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    print("about to print __name__...")
    print(__name__)   # this prints in terminal after running/refreshing the site
    return "No hablo queso!"

app.debug = True # If you get an error, the site will show you what it is.
app.run()
