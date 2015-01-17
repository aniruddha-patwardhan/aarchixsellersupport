from mongoengine import *
import datetime

class item_sku(Document):
    name = StringField(max_length = 50, required = True)
    title = StringField(max_length = 100, required = True)
    discription = StringField(max_length = 3000, required = True)

    image = URLField(verify_exist = True, required = True)
    image1 = URLField(verify_exist = True)
    image2 = URLField(verify_exist = True)
    image3 = URLField(verify_exist = True)
    image4 = URLField(verify_exist = True)

    brand = StringField(max_length = 50)

    mrp = IntField(min_value = 1)
    buy_price = IntField(min_value = 1, required = True)

    tags = ListField(StringField(), default = list)    
    attributes = DictField()

class service_sku(Document):
    name = StringField(max_length = 50, required = True)
    title = StringField(max_length = 100, required = True)
    discription = StringField(max_length = 3000, required = True)

    image = URLField(verify_exist = True, required = True)
    image1 = URLField(verify_exist = True)
    image2 = URLField(verify_exist = True)
    image3 = URLField(verify_exist = True)
    image4 = URLField(verify_exist = True)

    price = IntField(min_value = 1)

    tags = ListField(StringField(), default = list)    
    attributes = DictField()
