print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name3 = name1 + name2
name3 = name3.lower()
count1 = name3.count('t') + name3.count('r') + name3.count('u') + name3.count('e')


count2 = name3.count('l') + name3.count('o') + name3.count('v') + name3.count('e')

total = (count1 * 10) + count2

if(total < 10 or total > 90):
    print("Your score is "+str(total)+", you go together like coke and mentos.")
elif(40 < total < 50):
    print("Your score is "+str(total)+", you are alright together.")
else:
    print("Your score is "+str(total)+".")
