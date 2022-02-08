def sum_of_digits():
    two_digit_number_str = input("Type a two digit number: ")
    two_digit_number = int(two_digit_number_str)
    if(len(two_digit_number_str) != 2):
        print('Invalid input')
        return
    a = two_digit_number % 10
    b = int(two_digit_number / 10)
    return a+b

print(sum_of_digits())
