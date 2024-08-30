from enum import Enum


class status(Enum):
  ACTIVE = 1
  INACTIVE = 0


import pymysql
from book import *
import user as u

conn = None
cur = None


#constants for database columns
book_id = "bookid"
book_name = "title"
book_author = "author"
book_price = "price"
book_quantity = "quantity"

def get_connection():
  global conn, cur
  conn = pymysql.connect(host="localhost",
                         user="root",
                         password="",
                         database="books_mydb")
  cur = conn.cursor()

def close_connection():
  if conn is not None:
    cur.close()
    conn.close()

def save_user(user_name, password):
  insert_user_query = f"insert into users (username, password, status) values('{user_name}', '{password}', {status.ACTIVE.value})"    
  try:
    get_connection()
    cur.execute(insert_user_query)
    conn.commit()
  except Exception as e:
    print(e)
  finally:
    close_connection()

def get_user_status(user_name, password):
  status = None
  search_user_query = f"select status from users where username = '{user_name}' and password = '{password}'"    
  try:
    get_connection()
    cur.execute(search_user_query)
    rs = cur.fetchone()
    if rs is not None:
      status = rs[0]
    return status
  except Exception as e:
    print(e)
  finally:
    close_connection()

def add_book(bookname, author, price, quantity):
    insert_book_query =f"insert into books({book_name},{book_author},{book_price},{book_quantity}) values('{bookname}','{author}',{price},{quantity})"
    try:
      get_connection()
      cur.execute(insert_book_query)
      conn.commit()
    except Exception as e:
      print(e)
    finally:
      close_connection()

def get_books():
    select_books_query="select * from books"
    book_list = list()
    try:
      get_connection()
      cur.execute(select_books_query)
      rs = cur.fetchall()
      for row in rs:
        bk = book(row[0], row[1], row[2], row[3])
        book_list.append(bk)
      return book_list
    except Exception as e:
      print(e)
    finally:
      close_connection()

def get_book_by_id(bookid):
  select_book_query = f"select * from books where bookid = {bookid}"
  try:
    get_connection()
    cur.execute(select_book_query)
    data = cur.fetchone()
    return data
  except Exception as e:
    print(e)
  finally:
    close_connection()
  
def update_book(book_obj, quantity):
  update_book_query = f"update books set title = '{book_obj.get_title()}', author = '{book_obj.get_author()}', price = {book_obj.get_price()}, quantity = {quantity} where bookid = {book_obj.get_id()}"
  try:
    get_connection()
    cur.execute(update_book_query)
    conn.commit()
  except Exception as e:
    print(e)
  finally:
    close_connection()

def delete_book(bookid):
  delete_book_query=f"delete from books where bookid = {bookid}"
  try:
    get_connection()
    cur.execute(delete_book_query)
    conn.commit()
  except Exception as e:
    print(e)
  finally:
    close_connection()

def update_quantity(bookid):
  select_quantity=f"select quantity from books where bookid={bookid}"    
  try:
    get_connection()
    cur.execute(select_quantity)
    rs = cur.fetchone()
    current_qty = rs[0]
    if current_qty > 0:
      new_qty=current_qty-1
      update_bookqty_query = f"update books set quantity = {new_qty} where bookid = {bookid}"
      cur.execute(update_bookqty_query)
      conn.commit()
  except Exception as e:
    print(e)
  finally:
    close_connection()
