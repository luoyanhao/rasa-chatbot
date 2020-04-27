import mongoengine

from mongoengine import *
connect('adminDB', host='localhost', port=27017)
import datetime

class Title(EmbeddedDocument):
    title = StringField(required=True, max_length=200)

class Keyword(EmbeddedDocument):
    title = StringField(required=True)
    value = FloatField()

class User(Document):
    name = StringField(required=False, max_length=200)
    age = IntField(required=False)
    type = BooleanField(required=True, default=False)
    user_id = StringField(required=True, max_length=200)
    latesst_login = DateTimeField(required=True, default=datetime.datetime.now())
    diseases = ListField(EmbeddedDocumentField(Title))
    symptoms = ListField(EmbeddedDocumentField(Title))
    password = StringField(max_length=200)
    gender = IntField(default=2)

class Disease(Document):
    name = StringField(required=True, max_length=200)
    nick_name = ListField(EmbeddedDocumentField(Title))
    related_symptoms = ListField(EmbeddedDocumentField(Title))
    update_time = DateTimeField(required=True,  default=datetime.datetime.now())
    related_article = ListField(EmbeddedDocumentField(Title))
    related_music = ListField(EmbeddedDocumentField(Title))

class Symptom(Document):
    name = StringField(required=True, max_length=200)
    nick_name = ListField(EmbeddedDocumentField(Title))
    related_diseases = ListField(EmbeddedDocumentField(Title))
    update_time = DateTimeField(required=True, default=datetime.datetime.now())
    related_article = ListField(EmbeddedDocumentField(Title))
    related_music = ListField(EmbeddedDocumentField(Title))

class Article(Document):
    title = StringField(required=True, max_length=1000)
    content = StringField(required=True)
    channel = StringField(required=True, default='其他')
    hotness = IntField()
    keywords = ListField(EmbeddedDocumentField(Keyword))

class Music(Document):
    title = StringField(required=True, max_length=100)
    url = StringField(required=True)
    update_time = DateTimeField(required=True )
    related_dis = IntField()
    related_syms = IntField()
    keywords = ListField(EmbeddedDocumentField(Keyword))
class Log(Document):
    openid = StringField(required=True)
    count = IntField(required=True)
    content = StringField()
    articles = ListField(EmbeddedDocumentField(Title))
    music =ListField(EmbeddedDocumentField(Title))
class State(Document):
    openid = StringField(required=True)
    last_dialog = DateTimeField(required=True, default=datetime.datetime.now())
    current = IntField(required=True, default=1)
    task_state = BooleanField(required=True,default=False)
    symptoms = ListField(EmbeddedDocumentField(Title))
    index = IntField(required=True, default=0)
    need_age = BooleanField(required=True,default=False)
    need_gender = BooleanField(required=True, default=False)

class Reference(Document):
    key = StringField(required=True)
    value = StringField(required=True)
    type = IntField(required=True)

# temp = Reference(key = "社交恐惧症",value="社交恐惧症",type = 0)
# temp.save()
