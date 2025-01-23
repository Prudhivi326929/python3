a = int(input("Enter a number: "))
if a == 0 or a == 1:
    print("It's not a prime number.")
else:
    for i in range(2,5):
        if a%i == 0:
            print("Not a prime.")
            break
    else:
        print("It's prime")
