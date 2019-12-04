def whether(temp):
    if temp > 7:
        return "Warm"
    else:
        return "Cold"

user_input = float(input("Enter temparature: "))
print(whether(user_input))