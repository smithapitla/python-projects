def bubbleSort(numbers):
    swaps = 0
    for n in range(0, len(numbers)):
        if(n < len(numbers)-1):
            if(numbers[n] > numbers[n+1]):
                swap(numbers, numbers[n], numbers[n+1], n)
                swaps +=1

    #print('************************numbers after a round')
    #print(numbers)
    return swaps

def swap(numbers, a, b, n):
    temp = b
    numbers[n+1] = a
    numbers[n] = b


numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
print(numbers)
swaps = bubbleSort(numbers)
while(swaps > 0):
    swaps = bubbleSort(numbers)

print('**************')
print(numbers)
