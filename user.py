class user:

  def __init__(self, userid, username, password):
    self.__user_id__ = userid
    self.__user_name__ = username
    self.__password__ = password

  
  def set_id(self, userid):
    self.__user_id__ = userid

  def get_id(self):
    return self.__user_id__

  def set_username(self, username):
    self.__user_name__ = username

  def get_username(self):
    return self.__user_name__

  def set_password(self, password):
    self.__password__ = password

  def get_password(self):
    return self.__password__
