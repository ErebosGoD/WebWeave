from flask import Flask, redirect, render_template, url_for, request

app = Flask(__name__, template_folder='templates')


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run()