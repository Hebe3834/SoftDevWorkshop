# Team Whales: Hebe Huang, Josephine Lee, Han Zhang
# SoftDev
# K15: Sessions Greetings
# 2021-10-18

from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission
from flask import session           #facilitate sessions

#the conventional way:
#from flask import Flask, render_template, request

app = Flask(__name__)    #create Flask object


'''
trioTASK:
~~~~~~~~~~~ BEFORE RUNNING THIS, ~~~~~~~~~~~~~~~~~~
...read for understanding all of the code below.
Some will work as written; other sections will not. Can you predict which?
Devise some simple tests you can run to "take apart this engine," as it were.
Execute your tests. Process results.
PROTIP: Insert your own in-line comments wherever they will help your future self and/or current teammates understand what is going on.
'''

app.secret_key = "foo"

@app.route("/") #, methods=['GET', 'POST'])
def disp_loginpage():
    print("\n\n\n")
    print("***DIAG: this Flask obj ***")
    print(app)
    print("***DIAG: request obj ***")
    print(request)
    print("***DIAG: request.args ***")
    print(request.args)
    #print("***DIAG: request.args['username']  ***")
    #print(request.args['username'])
    print("***DIAG: request.headers ***")
    print(request.headers)
    return render_template( 'login.html' )


@app.route("/auth", methods=['GET', 'POST'])
def authenticate():
    print("\n\n\n")
    print("***DIAG: this Flask obj ***")
    print(app)
    print("***DIAG: request obj ***")
    print(request)
    print("***DIAG: request.args ***")
    print(request.args)
    #print("***DIAG: request.args['username']  ***")
    #print(request.args['username'])
    print("***DIAG: request.headers ***")
    print(request.headers)

    username = 'user'
    password = 'password'

    if request.method == 'POST': #conditional for 'POST' method or 'GET' method
        user = request.form['username']
        pas = request.form['password']
        if user == 'user':
            if pas == 'password':
                session['currentuser'] = request.form['username']
                return render_template('response.html',method = request.method, user = user)  #correct login
            else:
                return render_template('error.html', type = 'password') #returns password error
        else:
            return render_template('error.html', type = 'username') #returns username error
    else:
        user = request.args['username']
        pas = request.args['password']
        if request.args['username'] == 'user':
            if request.args['password'] == 'password':
                session['currentuser'] = request.args['username']
                return render_template('response.html',method = request.method, user = request.args['username'])  #correct login
            else:
                return render_template('error.html', type = 'password') #returns password error
        else:
            return render_template('error.html', type='username') #returns username error

@app.route("/logout?")
def logout():
    session.pop("currentuser")
    return render_template( 'login.html' )


    # returns response.html with the inputs method and user.


if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()
