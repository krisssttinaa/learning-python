# exception = events detected during execution that interrupt the flow of a programme
try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to devide by: "))
    result = numerator/denominator
except ZeroDivisionError as e:
    print(e)
    print("You can't devide by zero! lol") 
except ValueError as e:
    print(e)
    print("Enter only numbers please")
except Exception as e:
    print(e)
    print("Something went wrong")
else:
    print(result)
finally:
    print("This will always execute")