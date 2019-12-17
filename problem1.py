list1 = []
while True:

  username = input("Enter username: ")
  if username == "\end":
    break
  else:
    list1.append(username.capitalize())
    continue
print(" ".join(list1))
