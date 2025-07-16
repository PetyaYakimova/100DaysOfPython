from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("task1_bootstrap_card.html")


@app.route("/invite")
def invite():
    return render_template("birthday_invite_project.html")


if __name__ == "__main__":
    app.run(debug=True)
