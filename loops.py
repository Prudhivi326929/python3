temp = [1,2,3,4,5.1,9]
for i in temp:
  if(type(i)==int and i>2):
    print(i)

stu_grades = ["Marry":9.0, "Sim":8.8, ""John:7.4]
for i in stu_grades.items():#you can use keys() or values() to iterate
  print(i)
