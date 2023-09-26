# sort() method = used with lists
# sort() function = used with iterables

'''
students = ["Squidward", "Sandy", "Patrick", "Spongebob", "Mr. Krabs"]

students.sort()
print(students)
print()

students.sort(reverse=True)
print(students)
print()

pupils = ("Squidward", "Sandy", "Patrick", "Spongebob", "Mr. Krabs")
sorted_pupils = sorted(pupils, reverse=True)

for i in sorted_pupils:
    print(i)

'''

students = [("Squidward", "F", 60), 
            ("Sandy", "A", 33), 
            ("Patrick", "D", 36), 
            ("Spongebob", "B", 20), 
            ("Mr. Krabs", "C", 78)]

#sort by first column
students.sort()
for i in students: print(i)

#sort by key
grade= lambda grades:grades[1]
students.sort(key=grade, reverse=True)
for i in students: print(i)



pupils = (("Squidward", "F", 60), 
            ("Sandy", "A", 33), 
            ("Patrick", "D", 36), 
            ("Spongebob", "B", 20), 
            ("Mr. Krabs", "C", 78))
grade= lambda grades:grades[1]
sorted_pupils = sorted(pupils, key=grade)
for i in pupils: print(i)