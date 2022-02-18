import math
def prime_checker(number):
    
    if(number == 2):
        print("It's a prime number.")
    if(number%2 == 0):
        print("It's not a prime number.")
        return
    for a in range(3, int(math.sqrt(number)), +2):
        if(number%a == 0):
            print("It's not a prime number.")
            return
    print("It's a prime number.")

    
n = int(input("Check this number: "))
prime_checker(number=n)
