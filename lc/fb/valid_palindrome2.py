def isValidPalindrome(inputString):
    n = len(inputString)
    substring1 = inputString[0:n-1]
    substring2 = inputString[1:n]
    if(substring1 == substring1[::-1] or substring2 == substring2[::-1]):
        return True
    for i in range(0, n-1):
        substr = inputString[0:i] + inputString[i+1:]
        if(substr == substr[::-1]):
            return True
    return False

inputString = "aba"
print(inputString)
print(isValidPalindrome(inputString))

inputString =  "abca"
print(inputString)
print(isValidPalindrome(inputString))

inputString = "abc"
print(inputString)
print(isValidPalindrome(inputString))

inputString = "cbbcc"
print(inputString)
print(isValidPalindrome(inputString))

inputString = "eddze"
print(inputString)
print(isValidPalindrome(inputString))

inputString = "eccer"
print(inputString)
print(isValidPalindrome(inputString))
