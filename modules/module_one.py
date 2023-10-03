#*****************************************
# if __name__ == '__main__'
#*****************************************

# y tho?
# 1. Module can be run as a standalone program
# 2. Module can be imported and used by other modules

# Python interpreter sets "special variables", one of which is __name__
# then Python will execute the code found within __main__
# Python will assign the __name__ variable a value of ' __main__'
# the initial module being run name

def hello():
    print("Hello!")

'''
if __name__ == '__main__':
    print("running this module directly")
else:
    print("running other module indirectly")


#just run the module_one and module_two, and you will see diff results in terminal
'''

if __name__ == '__main__': hello()