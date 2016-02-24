from mongoengine import *

class Tweets(DynamicDocument):
    text = StringField(max_length=240)