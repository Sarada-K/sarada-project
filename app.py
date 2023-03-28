from flask import Flask, render_template

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
def index():
  return render_template("dashboard.html", books=BOOKS)


@app.route("/contactus")
def contactus():
  return render_template("contact-us.html")


@app.route("/aboutus")
def aboutus():
  return render_template("about-us.html")


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
