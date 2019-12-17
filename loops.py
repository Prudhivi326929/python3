temp = [1,2,3,4,5.1,9]
for i in temp:
  if(type(i)==int and i>2):
    print(i)

stu_grades = ["Marry":9.0, "Sim":8.8, ""John:7.4]
for i in stu_grades.items():#you can use keys() or values() to iterate
  print(i)
phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
for i in phone_numbers.values():
    print(i.replace("+","00"))

username = ''
while username != "pypy":
  username = input("Enter user name: ")
  
while True:
  username = input("Enter username: ")
  if username == "pypy":
    break
  else:
    continue
