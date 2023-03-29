from enum import Enum


class status(Enum):
  ACTIVE = 1
  INACTIVE = 0


import pymysql

conn = None
cur = None


def get_connection():
  global conn, cur
  conn = pymysql.connect(host="0.0.0.0",
                         user="root",
                         password="",
                         database="books_mydb")
  cur = conn.cursor()

  def close_connection():
    if conn is not None:
      cur.close()
      conn.close()

  def save_user(user_id, password):
    try:
      get_connection()
      insert_user_query = "insert into users values(user_id, password, status.ACTIVE.value)"
      cur.execute(insert_user_query)
      conn.commit()
    except Exception as e:
      print(e)
    finally:
      close_connection()
