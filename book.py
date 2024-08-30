class book:

  def __init__(self, bookid, title, author, price, rating = None):
    self.__id__ = bookid
    self.__title__ = title
    self.__author__ = author
    self.__price__ = price
    self.__rating__ = rating

  
  def set_id(self, bookid):
    self.__id__ = bookid

  def get_id(self):
    return self.__id__

  def set_title(self, title):
    self.__title__ = title

  def get_title(self):
    return self.__title__

  def set_author(self, author):
    self.__author__ = author

  def get_author(self):
    return self.__author__

  def set_price(self, price):
    self.__price__ = price

  def get_price(self):
    return self.__price__

  def set_rating(self, rating):
    self.__rating__ = rating

  def get_rating(self):
    return self.__rating__

