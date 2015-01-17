from mongoengine import *
from users import * #bcoz we will reference user object in orders
import datetimeu

connect('sellersupport')

class order_item(EmbeddedDocument):
    sku = ReferenceField(sku, required = True)
    quantity = IntField(default = 1, required = True)
    item_price = IntField(default = 1, required = True)
    shipping_price = IntField(default = 1, required = True)
    service = ReferenceField(service_sku)

class order(Document):
    user = ReferenceField(user)
    items = ListField(EmbeddedDocumentField(order_item))

    channel = StringField(max_length = 50, required = True)
    orderdate = DateTimeField(default = datetime.datetime.now())

    price = IntField(default = 1, required = True)

    last_name = StringField(max_length = 50, required = True)
    email = EmailField(max_length = 100, required = True, default = "girlzfashionz@gmail.com")
    phone1 = StringField(max_length = 10, required = True)
    phone2 = StringField(max_length = 10)
    address = StringField(max_length = 1000, required = True)
    city = StringField(max_length = 50, required = True)
    state = StringField(max_length = 50, required = True)
    pin = StringField(max_length = 6, required = True)
    country = StringField(max_length = 50, required = True, default = "India")
    anniversary = DateTimeField(default = datetime.datetime.now())
    gender = StringField(max_length = 6, required = True, default = "female")



