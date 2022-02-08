import math

def largestPrimeFactor(num):
  largest_prime = -1
  while(num % 2 == 0):
    largest_prime = 2
    num >>= 1 

  for a in range(3, int(math.sqrt(num)), +2):
    while(num % a == 0):
      largest_prime = a
      num = num / a
  
  if(num > 2):
    largest_prime = num

  return largest_prime


print(largestPrimeFactor(13195))
print(largestPrimeFactor(600851475143))
