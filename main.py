from flask import Flask, request, redirect, render_template
import cgi
import os
import re

app = Flask(__name__)
app.config['DEBUG'] = True

regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

def check(email):
    if(re.search(regex,email)):
        return True
    else:
        return False

@app.route('/signup')
def display_time_form():
    return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def validate_form():

    username = request.form['username']
    password = request.form['password']
    vpassword = request.form['vpassword']
    email = request.form['email']

    username_error = ''
    password_error = ''
    vpassword_error = ''
    email_error = ''

    if len(username) < 3 or len(username) > 20 :
        username_error = 'Username must be between 3 and 20 characters'
        username = ''
        password = ''
        vpassword = ''
    elif " " in username:
        username_error = 'You cannot have spaces in your username'
        username = ''
        password = ''
        vpassword = ''
    else:
        username = request.form['username']

    if len(password) < 3 or len(password) > 20:
        password_error = 'Password must be between 3 and 20 characters'
        password = ''
        vpassword = ''
    elif " " in password:
        password_error = 'You cannot have spaces in your password'
        password = ''
        vpassword = ''
    else:
        if len(vpassword) == 0:
            vpassword_error = 'You must verify your password.'
            password = ''
        elif password != vpassword:
            vpassword_error = 'Your passwords do not match.'
            password = ''
            vpassword = ''
        else:
            password = request.form['password']
    if len(email)>0 and check(email)==False:
        email_error = 'Enter a valid email address'
        email = ''
        password = ''
        vpassword = ''




    if not username_error and not password_error and not vpassword_error and not email_error:
        username = username
        return redirect('/welcome?username={0}'.format(username))
    else:
        return render_template('signup.html', username_error=username_error,
            password_error=password_error,
            vpassword_error=vpassword_error,
            email_error=email_error,
            username=username,
            password=password,
            vpassword=vpassword)


@app.route("/welcome")
def hello():
    username = request.args.get('username')

    return render_template('welcome.html', username=username)

    




app.run()

