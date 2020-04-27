from pymongo import MongoClient
from mongoengine import *
class DBService():
    def __init__(self):
        self.ip = 'localhost'
        self.port = 12
        connect('adminDB', host='localhost', port=27017)



