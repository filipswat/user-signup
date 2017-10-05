from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config["DEBUG"] = True

@app.route("/")
def user_form():
    return render_template("user-signup.html")

@app.route("/", methods=["POST"])
def validate():
    username = request.form["username"]
    password = request.form["password"]
    verify = request.form["verify"]
    email = request.form["email"]

    return render_template("user-confirmation.html", username=username,
    password=password, verify=verify, email=email)

app.run()