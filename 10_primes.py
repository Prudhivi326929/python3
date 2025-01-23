def is_prime(num):
    for i in range(2,num):
        if num%i ==0:
            return False
    return True
def main():
    count = 0
    num = 2
    while count <10:
        if is_prime(num):
            print(num)
            count+=1
        num+=1
if __name__ == "__main__":
    main()
    
