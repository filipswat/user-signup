from flask import Flask, request, redirect, render_template
import cgi

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

    username = request.form["username"]
    password = request.form["password"]
    verify = request.form["verify"]
    email = request.form["email"]

    if not username:
        error_count += 1
        name_error = "Please enter a valid username"

    if not password:
        error_count += 1
        password_error = "Please enter a valid password"
    else:
        if password != verify:
            error_count += 1
            verify_error = "Passwords do not match"
    
    if email:
        if "a" not in email:
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