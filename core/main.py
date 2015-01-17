from users import *

connect('sellersupport')

anix = user(first_name = "Anix", last_name = "pats", phone1="9902465002", address="DSR elegance", city="bangalore", state="karnataka", pin="560034", gender="male").save()

print "doc saved"
for usr in user.objects():
    print usr.first_name
    usr.delete()
