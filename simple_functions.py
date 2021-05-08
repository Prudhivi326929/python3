def additions(a,b):
    return a+b

print(additions(-5,6))
print("hello")

def shuttering_output(string):
    new_str = ""
    new_str = new_str + string[:2] + "..." + " " +string[:2] + "..." + " " + string[2:] + "?"
    return new_str

print(shuttering_output("enthusiastic"))
