from flask import Flask, request, redirect, render_template
import cgi
import re

app = Flask(__name__)

app.config["DEBUG"] = True

@app.route("/")
def user_form():
    return render_template("user-signup.html")

@app.route("/", methods=["POST"])
def validate():
    error_count = 0

    name_error = ""
    password_error = ""
    verify_error = ""
    email_error = ""

    valid_username = re.compile(r"^[\w]{3,20}$")
    valid_password = re.compile(r"^[\w]{3,20}$")
    valid_email = re.compile(r"^[a-zA-Z0-9\.]+@[\w]+\.[\w]+")

    username = request.form["username"]
    password = request.form["password"]
    verify = request.form["verify"]
    email = request.form["email"]

    if not valid_username.match(username):
        error_count += 1
        name_error = "Please enter a valid username (3-20 characters, no spaces)"

    if not valid_password.match(password):
        error_count += 1
        password_error = "Please enter a valid password (3-20 characters, no spaces)"
    else:
        if password != verify:
            error_count += 1
            verify_error = "Passwords do not match"
    
    if email:
        if not valid_email.match(email):
            error_count += 1
            email_error = "Please enter a valid email"

    if error_count == 0:
        return render_template("user-confirmation.html",
        username=username, password=password, verify=verify, email=email)
    else:
        return render_template("user-signup.html",
        username=username, email=email,
        name_error=name_error, password_error=password_error,
        verify_error=verify_error, email_error=email_error)

    

app.run()