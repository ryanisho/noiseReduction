from flask import Flask, redirect, render_template, request, url_for, send_file
import os

app = Flask(__name__)

UPLOAD_FOLDER = './images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def index():
    if request.method == "POST":



    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
