# zip(*iterables) = aggregate elements from two or more iterables (list, tuples, sets, etc.)
#                   creates a zip object with paired elements stored in tupes for each element

usernames = ["Dude", "Bro", "Mister"]
passwords = ("p@ssword", "abc123", "guest")

users = zip(usernames, passwords)
print(type(users))
for i in users: print(i)

users = list(zip(usernames, passwords))
print(type(users))

users = dict(zip(usernames, passwords))
print(type(users))
for key,value in users.items(): print(key+' '+value)

login_date = ["1/1/2021", "1/2/2021", "1/3/2021"]
usersss = zip(usernames, passwords, login_date)
for i in usersss: print(i)