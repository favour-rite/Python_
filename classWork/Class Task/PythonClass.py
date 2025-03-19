import string

names = ['esther','bimbola','moses']

print("-".join(names))

#print(names.isalnum(names))

username = input("Enter your name: ")
if username.isspace():
    username = input("Enter your name: ")
    