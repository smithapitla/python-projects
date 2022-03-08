def bubbleSort(numbers):
    length_of_numbers = len(numbers)
    for i in range (0, length_of_numbers-1 ):
        for j in range (0, length_of_numbers-1):
            if(numbers[j] > numbers[j+1]):
                temp = numbers[j+1]
                numbers[j+1] = numbers[j]
                numbers[j] = temp


numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
print(numbers)
bubbleSort(numbers)
print(numbers)
