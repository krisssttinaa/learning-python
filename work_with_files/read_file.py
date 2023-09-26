try:
    with open("/Users/krisss/Desktop/temp.txt") as file:
        print(file.read())
    print(file.closed)
except FileNotFoundError:
    print("That file was not found")
