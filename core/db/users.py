from mongoengine import *
import datetime

# sellerid is required in all collections to ensure system is multitenant

# making address top class document and not subdocument as we want to do analytics on addresses
# will mantain cross reference to user list in address as one address can also belong to many users
# we want to query address by following ways
#   1. All users in given city, state, pin, geo etc
class address(Document):
    address = StringField(max_length = 1000, required = True)
    city = StringField(max_length = 50, required = True)
    state = StringField(max_length = 50, required = True)
    pin = StringField(max_length = 6, required = True)
    country = StringField(max_length = 50, required = True, default = "India")

    users = ListField(ReferenceField(user))
    seller_id = StringField(max_length = 100, required = True)


# We want to query user by following dimensions
#   1. All users with dob/anniversary in given month
#   2. all males/females with a age
#   3. all users from a certain address etc
class user(Document):
    first_name = StringField(max_length = 50, required = True)
    last_name = StringField(max_length = 50, required = True)
    email = EmailField(max_length = 100, required = True, default = "girlzfashionz@gmail.com")
    phone1 = StringField(max_length = 10, required = True)
    phone2 = StringField(max_length = 10)

    addresses = ListField(ReferenceField(address), required = True)

    dob = DateTimeField(default = datetime.datetime.now())
    anniversary = DateTimeField(default = datetime.datetime.now())
    gender = StringField(max_length = 6, required = True, default = "female")
    
    seller_id = StringField(max_length = 100, required = True)
