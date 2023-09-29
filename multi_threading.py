# thread = a flow of execution. Like a separate order of instructions.
#          However each thread takes a turn running to achieve concurrency
#          GIL = (global interpreter lock), 
#          allows only one thread to hold the control of the Python interpreter at any one time

# cpu bound = program/task spends most of it's time waiting for internal events (CPU intensive)
#             use multiprocessing

# io bound = program/task spends most of it's time waiting for external events (user input, web scraping)
#            use multithreading

import threading
import time

def eat_breakfast():
    time.sleep(3)
    print("You ate breakfast")

def drink_coffee():
    time.sleep(4)
    print("You drank coffee")

def study():
    time.sleep(5)
    print("You finish studying")

x= threading.Thread(target=eat_breakfast, args=()) 
x.start()

y= threading.Thread(target=drink_coffee, args=()) 
y.start()

z= threading.Thread(target=study, args=()) 
z.start()

#now we make a main thread to join and finish, and only then main one can proceed
#x.join()
#y.join()
#z.join()

#eat_breakfast()
#drink_coffee()
#study()

print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())

#now the execution is not sequentional and we have 3 threads cuncurently running
#main thread will continue to his set of instructions to active count etc
#and it finished his tasks before threads x, y, z