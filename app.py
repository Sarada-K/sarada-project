from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
  return render_template("dashboard.html")


@app.route("/contactus")
def contactus():
  return render_template("contact-us.html")


@app.route("/aboutus")
def aboutus():
  return render_template("about-us.html")


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
