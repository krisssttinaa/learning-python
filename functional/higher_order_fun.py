#Higher prder functions
'''
def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

def hello(func):
    text = func("Hello")
    print(text)

hello(loud)
'''

def divisor(x):
    def dividend(y):
        return y/x
    return dividend

divide = divisor(2)
print(divide(10))

#firstly we pass 2 to divisor, and return a divident
#in a print we pass 10 to divident 
#and we get 5