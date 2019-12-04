import datetime
x=datetime.datetime.now()
#print(x)

number = 10
word = "hello"
print(number, word)
x = 10
y = 10.5
z = "string"
student_grades = [1,2,3]

#print(type(x), type(y), type(z), type(student_grades))
#print(list(range(1,10))) #[1,2,3,4,5,6,7,8,9]
#print(list(range(1,10,2))) #[1,3,5,7,9]

#print(dir(list)) #lists all possible methods with type "list"

"""
List Methods
mysum = sum(student_grades)
length = len(student_grades)
mean = mysum/length
print(mean)
print(student_grades.count(1))
student_grades.append(10)
student_grades.remove(2)
"""

"""
Dictionaries
student_grades = {"marry":9.1, "john":7.5}
print(student_grades)
print(student_grades.values())
print(student_grades.keys())
"""

temp_tuple = (1,4,5)
#tuples are immutable. Means we can't add values to tuple once created.

print(dir(__builtins__)) # to print Python builtin functions


