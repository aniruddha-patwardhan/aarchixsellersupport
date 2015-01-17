from users import *

connect('sellersupport')

anix_address = address(address="DSR elegance", city="bangalore", state="karnataka", pin="560034", gender="male")
anix = user(first_name = "Anix", last_name = "pats", phone1="9902465002", addresses=[anix_address], gender="male")
anix.save()

print "doc saved"
for usr in user.objects():
    print usr.first_name, usr.addresses
    usr.delete()
