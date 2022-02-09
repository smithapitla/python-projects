print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
price = 0
if(size == 'S' or size == 's'):
    price = 15
    if(add_pepperoni == 'Y' or add_pepperoni == 'y'):
        price = price + 2
elif (size == 'M' or size == 'm'):
    price = 20
    if(add_pepperoni == 'Y' or add_pepperoni == 'y'):
        price = price + 3
elif (size == 'L' or size == 'l'):
    price = 25
    if(add_pepperoni == 'Y' or add_pepperoni == 'y'):
        price = price + 3

if(extra_cheese == 'Y' or extra_cheese == 'y'):
    price = price + 1

print(f'Your final bill is: $'+str(price))
