from mongoengine import *
import datetime

class address(EmbeddedDocument):
    address = StringField(max_length = 1000, required = True)
    city = StringField(max_length = 50, required = True)
    state = StringField(max_length = 50, required = True)
    pin = StringField(max_length = 6, required = True)
    country = StringField(max_length = 50, required = True, default = "India")


class user(Document):
    first_name = StringField(max_length = 50, required = True)
    last_name = StringField(max_length = 50, required = True)
    email = EmailField(max_length = 100, required = True, default = "girlzfashionz@gmail.com")
    phone1 = StringField(max_length = 10, required = True)
    phone2 = StringField(max_length = 10)

    addresses = ListField(EmbeddedDocumentField(address), required = True)

    dob = DateTimeField(default = datetime.datetime.now())
    anniversary = DateTimeField(default = datetime.datetime.now())
    gender = StringField(max_length = 6, required = True, default = "female")
