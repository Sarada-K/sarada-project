from flask import Flask, render_template, redirect, request

app = Flask(__name__)
BOOKS = [{
  "id": 1,
  "title": "1984",
  "author": "George Orwell",
  "price": "Rs. 100",
  "rating": 4.9
}, {
  "id": 2,
  "title": "The Lord of the Rings",
  "author": "R.R. Tolkien",
  "price": "Rs. 2300",
  "rating": 4.9
}, {
  "id": 3,
  "title": "The Kite Runner",
  "author": "Khaled Hosseini",
  "price": "Rs. 357",
  "rating": 4.7
}, {
  "id": 4,
  "title": "Harry Potter and the Philosopher’s Stone",
  "author": "J.K. Rowling",
  "price": "Rs. 420",
  "rating": 5
}, {
  "id": 5,
  "title": "Slaughterhouse-Five",
  "author": "Kurt Vonnegut",
  "price": "Rs. 524",
  "rating": 4.6
}]


@app.route("/")
def login():
  return render_template("home.html", type="initial")


@app.route("/signup")
def signup():
  return render_template("home.html", type="signup")


@app.route("/login", methods=['POST'])
def hello_user():
  name = request.form['user']
  if name.strip() == 'admin':
    return redirect("/user/admin/")
  else:
    return redirect("/user/")


@app.route("/user/admin/")
def admin_index():
  return render_template("admin_dashboard.html", books=BOOKS, type='admin')


@app.route("/user/")
def guest_index():
  return render_template("guest_dashboard.html", books=BOOKS, type='others')


@app.route("/contactus")
def contactus():
  return render_template("contact-us.html")


@app.route("/aboutus")
def aboutus():
  return render_template("about-us.html")


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
