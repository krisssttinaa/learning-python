import random
#functions
def hello(name):
    print("hello! "+ name)
    pass

hello("dude")

#####################
#return value
def multiply(n1, n2):
    return n1*n2

x=multiply(6,8)
print(x)


####################
#keyword arguments
def helloo(first, middle, last):
    print("Hello "+first+" "+middle+" "+last)

helloo(last="Piiarska", middle="Dude", first="Kris")


###################
#nested function calls
# num = input ("Enter a whole positive number: ")
# num = float (num)
# num = abs (num)
# num = round (num)
# print (num)

print(round (abs (float (input ("Enter a whole positive number: ")))))

###################
#scope
#LEGB Local, Enclosing, Global, Built-in
###################


#*args = parameter that will pack all arguments into a tuple
#        function can accept a varying amount of arguments
'''
def add(*args):
    sum=0
    for i in args:
        sum+=i
    return sum

print(add(1,2,3,4,5,6))
'''
def add(*stuff):
    sum=0
    stuff=list(stuff) #because tupes are immutable, lists aren't
    stuff[0]=0
    for i in stuff:
        sum+=i
    return sum

print(add(1,2,3,4,5,6))


###################
#**kwargs = parameter that will pack all the arguments into a dictionary
#           functions can accept a varying amount of arguments
'''
def hi(**kwards):
    print("Hello "+kwards['first']+" "+ kwards['last'])
hi(first="Kris", middle="Dude", last="Piiarska")
'''

def hi(**kwards):
    for key,value in kwards.items():
        print(value, end=" ")
hi(title="Ms.", first="Kris", middle="Dude", last="Piiarska")
#and now we can just add title="Ms." and no errors, we are fine


####################
#str.format() = method, gives users mpre control when displaying

animal = "cow"
item= "moon"

#print("The "+animal+" jumped over the "+item)
print("The {} jumped over the {}".format(animal,item))
#print("The {1} jumped over the {0}".format(animal,item)) #for reverse
#print("The {item} jumped over the {animal}".format(animal="cow",item="moon")) #keyword

text = "The {} jumped over the {}"
print(text.format(animal, item))

name="Kris"
print("Hello, my name is {}".format(name))
print("Hello, my name is {:10}. Nice to meet you".format(name))
print ("Hello, my name is {:<10}. Nice to meet you".format(name))
print("Hello, my name is {:>10}. Nice to meet you".format(name))
print ("Hello, my name is {:^10}. Nice to meet you".format(name))

number = 314159
print("The number pi is {:.3f}".format(number)) #3first digits after . = 314159.000
print("The number pi is {:,}".format(number)) #comma after first = 1,000
print("The number pi is {:b}".format(number)) #binary
print("The number pi is {:o}".format(number)) #1750
print("The number pi is {:X}".format(number)) #hexa = 3E8
print("The number pi is {:E}".format(number)) #1.000000E+03


######################
#preudo random
x=random.randint(1,6)
print(x)
y=random.random() #random btw 0 and 1

myList=['rock', 'paper', 'scissors']
z=random.choice(myList)

cards=[1,2,3,4,5,6,7,8,9,"J","Q","K","A"]
random.shuffle(cards)
print(cards)