from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config["DEBUG"] = True

@app.route("/")
def user_form():
    return render_template("user-signup.html")

app.run()