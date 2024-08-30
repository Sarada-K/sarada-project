from flask import Flask, render_template, redirect, request
import database as db
import requests
from bs4 import BeautifulSoup
from enum import Enum
from book import *


app = Flask(__name__)

class book_rating(Enum):
  One = 1
  Two = 2
  Three = 3
  Four = 4
  Five = 5
  NOT_APPLICABLE = 'NA'


@app.route("/")
def login():
  return render_template("home.html", type="initial")


@app.route("/signup")
def signup():
  return render_template("home.html", type="signup")


@app.route("/login/", methods=['POST'])
def hello_user():
  name = request.form['user']
  pwd = request.form['pwd']
  if request.form['send'] == 'sign-up':
    db.save_user(name, pwd)
    if name.strip() == 'admin':
      return redirect("/user/admin/")
    else:
      return redirect("/user/")
  elif request.form['send'] == 'login':
    status = db.get_user_status(name, pwd)
    if status == 1:
      if name.strip() == 'admin':
        return redirect("/user/admin/")
      else:
        return redirect("/user/")
    else:
        return render_template("home.html",type="initial", message = "invalid username or password")

@app.route("/create", methods=["POST"])
def addbook():
  return render_template("create.html")

@app.route("/store", methods=['POST'])
def store():
    bookname = request.form['bookname']
    author = request.form['author']
    price = request.form['price']
    quantity = request.form['quantity']    
    db.add_book(bookname, author, price, quantity)
    return redirect("/user/admin/")

@app.route("/user/admin/")
def admin_index():
  book_list = db.get_books()
  return render_template("admin_dashboard.html", books=book_list, type='admin')


@app.route("/user/")
def guest_index():
  rating = None
  book_list = db.get_books()
  ratings = get_ratings()
  for book in book_list:
    title = book.get_title()
    rating = ratings.get(title)
    if rating is not None:
      book.set_rating(book_rating[rating].value)
    else:
      book.set_rating(book_rating['NOT_APPLICABLE'].value)
  return render_template("guest_dashboard.html", books=book_list, type='others')


@app.route("/contactus")
def contactus():
  return render_template("contact-us.html")


@app.route("/user/aboutus")
def aboutus():
  return render_template("about-us.html")

@app.route("/edit/<id>")
def edit(id):
  data = db.get_book_by_id(id)
  return render_template("editform.html", d = data)

@app.route("/update<bookid>", methods=['POST'])
def update(bookid):
  bname = request.form['bookname']
  author = request.form['author']
  price = request.form['price']
  quantity = request.form['quantity']
  book_obj = book(bookid, bname, author, price)
  db.update_book(book_obj, quantity)
  return redirect("/user/admin/")

@app.route("/delete/<bookid>")
def delete(bookid):
  db.delete_book(bookid)
  return redirect("/user/admin/")

@app.route("/update_qty/<bookid>")
def update_qty(bookid):
  db.update_quantity(bookid)
  book_list = db.get_books()
  return render_template("guest_dashboard.html", books=book_list, type='others', message="Your order is successful!!Thank you for shopping with us!")
  

def get_ratings():
  d = dict()
  site = requests.get("http://books.toscrape.com/index.html")
  soup = BeautifulSoup(site.content, 'html.parser')
  li = soup.findAll('li', class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")
  for book in li:      
      title = book.img.attrs['alt']
      article = book.find('article', class_='product_pod')
      para = article.p
      rating = para['class'][1]
      d[title] = rating
  return d

if __name__ == '__main__':
  app.run(debug=True)
