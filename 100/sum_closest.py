import math
def sum_closest_to_number(numbers, number):
    leftIndex = 0
    rightIndex = len(numbers)-1
    numbers.sort()
    print(numbers)
    while(leftIndex <= rightIndex):
        numberOne = numbers[leftIndex]
        numberTwo = numbers[rightIndex]
        returnValue = [numberOne, numberTwo]
        currentSum = numberOne + numberTwo
        if(currentSum < 0):
            leftIndex += 1
        elif(currentSum > 0):
            rightIndex -=1
        else:
            return returnValue
    
numbers = input("Input a list of numbers").split()
sum_closest_to = int(input("Find 2 integers whose sum is closest to?"))
print(numbers)
for n in range(0, len(numbers)):
  numbers[n] = int(numbers[n])
  
print(sum_closest_to_number(numbers, sum_closest_to))
