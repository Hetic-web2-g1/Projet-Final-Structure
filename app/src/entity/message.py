# from email.mime import base
# from sqlalchemy import Column, Integer, String, null

# from src.database.db_engine import *

# class Message():

#     def __init__(self, id_user = null, id_field = null, id_event = null, message_type = null, content = null):
#         self.id_user = id_user
#         self.id_field = id_field
#         self.id_event = id_event
#         self.message_type = message_type
#         self.content = content

#     def get_age(self):
#          print("getter method called")
#          return self._age
       
#      # function to set value of _age
#     def set_age(self, a):
#         print("setter method called")
#         self._age = a

#     __tablename__ = 'message'
#     id = Column(Integer, primary_key=True)
#     id_user = Column(Integer, nullable=True)
#     id_field = Column(Integer, nullable=True)
#     id_event = Column(Integer, nullable=True)
#     message_type = Column(String(255))
#     content = Column(String(255))
    
#     def __repr__(self):
#         return "<Message(id_user='%s', id_field='%s', id_event='%s', type='%s', content='%s')>" % (self.id_user, self.id_field, self.id_event, self.type, self.content)
    

# msg = Message(is_user=1, id_field=null, id_event=null, type="user", content="content")