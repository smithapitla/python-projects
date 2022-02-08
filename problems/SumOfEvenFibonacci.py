def sumOfEvenFibonacci(limit):
  first = 0
  result = 0
  second = 2
  total = 2

  for a in range(0, limit, +1):
    result = first + ( 4 * second)
    if(result > limit):
      break;
    total = total + result
    first = second
    second = result
  return total
  
print(sumOfEvenFibonacci(4000000))
