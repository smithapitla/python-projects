
import random
#test_seed = int(input("Create a seed number: "))
#random.seed(test_seed)

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
length = len(names)
random_name = random.randint(1, length)
print(names[random_name-1]+" is going to buy the meal today!")
