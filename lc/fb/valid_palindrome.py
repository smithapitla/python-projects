def isValidPalindrome(inputString):
    reverse = inputString[::-1]
    if(reverse == inputString):
        return True
    head = 0
    tail = len(inputString)-1
    misMatchCount = 0
    for i, current_char in enumerate(inputString):
        if(i < tail):
            if(current_char == inputString[tail]):
                tail -=1
            else:
                misMatchCount+=1
    if(misMatchCount == 1):
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
