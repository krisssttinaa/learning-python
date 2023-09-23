import math
import time

print("Hello World!")

my_name = 7
my_name = str(my_name)
print("Hello and welcome " + my_name + "!")

#this is the first comment, whatever

"""
this way you write multiple comments
"""

print(type(my_name))

first_name = "Krisss"
last_name = "Piiarska"
full_name = first_name+" "+last_name
print(full_name)

#age = 21
#age +=1 
#print ("Your age is: "+str(age))
#print (type(age))
height = 250.5
print (height)
print (type(height))

#DATA TYPES: usual int, float, bool, string


#MULTIPLE ASSIGNMENT allows us to assign multiple variables lat the same time in one line of code

# name = "Bro"
# age = 21
# attractive = True

#print (name)
#print (age)
#print (attractive)

# Spongebob = 30
# Patrick = 30
# Sandy = 30
# Squidward = 30

Spongebob = Patrick = Sandy = Squidward = 30
print(Sandy)

list = [1,2,3,4,5]

list = list[::-1] #slicing
print(list)

str0 = 'im string'
str0 = str0[::-1]
print(str0)

str1 = 'notsunnyday'
str1= str1[3:]
print(str1)


#STRING METHODS
print(len(str1))
print(str1.find("o"))
print(str1.capitalize())
print(str1.upper())
print(str1.lower())
print(str1.isdigit())
print(str1.isalpha())
print(str1.count("o"))
print(str1.replace("o", "a"))
print(str1*3) #toprint 3 times


#TYPECASTING
x=1
y=2.0
z="3"

y = int(y)
z=int(z)
z=float(z)
z= str(z)

print(x)
print(y)
print(z)

print("X is "+str(x))


#USER INPUT
""""
name=input("What is your name?: ")
print("Hello "+name)

age= int(input("How old are you?: "))
age = age+2
print("You will be "+str(age)+" years old in 2 years")
"""

#MATH FUNCTIONS
pi = 3.14
x=1
y=2
z=3

print(round(pi)) #nearest int
print(math.ceil(pi)) #up
print(math.floor(pi))
print(abs(pi))
print(pow(pi, 2))
print(math.sqrt(20))
print(max(x,y,z))


#SLICING THE STRING
# create a substring by extracting elements from another string
# indexing[] or slice ()
# [start: stop: step] 
# [inclusive : exclusive : by how much increase the index]

name = "Kris Piiarska"
#fst_name = name[3] #- to slice only one letter from a string
fst_name = name[:4]
print(fst_name)

lst_name = name[5:]
print(lst_name)

funky_name = name[0:8:2]
#funky_name = name[::2] - is the same
print(funky_name)

reversed_name = name[::-1]
print(reversed_name)

###########
website = "http://google.com"
website1 = "http://wikipedia.com"
slice = slice(7,-4)

print(website[slice])
print(website1[slice])


###########################
temp = int(input("What is the temperature outside?: "))

if not(temp>=0 and temp <=30) :
    print("the temperature is good today!")
elif not(temp<0):
    print("the temperature is bad today!")
else:
    print()


#############################
name = ""

while len(name) == 0:
    name = input("Enter your name: ")

print("Hello "+name)


#############################
"""
for i in range(10):
    print(i+1)

for j in range(50):
    if j%2==0: 
        print(j)

for k in range(50,100+1, 2): #inclusive, exclusive
    print(k)

for g in "Krisss Piiaska":
    print(g)

for second in range(10, 0, -1):
    print(second)
    time.sleep(1)
print("Happy new year")
"""


#############################
#Loop control Statements = change a loops execution from its normal sequence
# break =    used to terminate the loop entirely
""""
while True:
    name = input("Enter your name: ")
    if name != "":
        break
"""
# continue = skips to the next iteration of the loop
phone_num = "123-456-7890"
for i in phone_num:
    if i=="-":
        continue
    print(i, end="") #end="" for avoiding printing from a new line
# pass =     does nothing, acts like a placeholder
for i in range(1,21):
    if i==13:
        pass
    else:
        print(i)


##########################
#list = to store multiple items in a single var

food= ["pizza", "hamburger", "hotdog", "spagetti"]
food[0]="sushi"
print(food[0])

for x in food:
    print(x)

food.append("ice cream")
food.remove("hotdog")
food.pop()
food.insert(0, "cake")
food.sort()
#food.clear()
print(food)

#########################
#2D lists = a list of lists
drinks = ["coffee", "tea"]
main_food = ["salad", "fish"]
desert = ["ice cream", "tiramisu"]

dinner = [drinks, main_food, desert]
print(dinner)


##########################
# tuple = collection which is ordered and unchangeble
#         used to group together related data
student = ("Chris", 20, "male" )
print(student.count("Chris"))
print(student.index("male"))

for x in student:
    print(x, end=", ")

if "Chris" in student:
    print("Chris is here")


###########################
#set = collection which is unordered, unindexed, no dups
utensils = {"fork", "spoon", "knife"}
dishes = {"bowl", "plate", "cup"}

print(utensils.difference(dishes))
print(utensils.intersection(dishes))

utensils.add("napkin")
utensils.remove("fork")
#utensils.clear()
utensils.update(dishes)

for x in utensils:
    print(x)

dinner_table = utensils.union(dishes)


##########################
# dictionary = a changeable=, unordered collection of unique key-value pairs
#              fast necause they use hasing, allow us to access a value quikly
capitals = {'USA': 'Washington DC',
            'India': 'New Dehli',
            'China': 'Beijing',
            'Slovenia': 'LJ'}
print(capitals['Slovenia'])
print(capitals.get('Germany')) # is safer way than upper one, because no error
print(capitals.keys())
print(capitals.values())
print(capitals.items())

for key,value in capitals.items():
    print(key, value)

###changing is possible - mutable!
capitals.update({'Germany': 'Berlin'})
capitals.update({'USA': 'Las Vegas'})
capitals.pop('China')
capitals.clear()


############################
name = "Kris Piiarska"
if(name[0].islower()):
    name = name.capitalize()
print(name)

first_nameee = name[:4].upper()
print(first_nameee)
last_nameee = name[5:].upper()
print(last_nameee)
last_char = name[-1]