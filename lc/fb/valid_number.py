def isValidNumber(inputString):
    seen_digit = seen_exponent = seen_dot =  False
    for i, current_char in enumerate(inputString):
        if current_char.isdigit():
            seen_digit = True
        elif current_char in ["+", "-"]:
            if i > 0 and inputString[i - 1] != "e" and inputString[i - 1] != "E":
                return False
        elif current_char in ["e", "E"]:
            if seen_exponent or not seen_digit:
                return False
            seen_exponent = True
            seen_digit = False
        elif current_char == ".":
            if seen_dot or seen_exponent:
                return False
            seen_dot = True
        else:
            return False
    
    return seen_digit

inputString = "0089"
print(inputString)
print(isValidNumber(inputString))

inputString =  "95a54e53"
print(inputString)
print(isValidNumber(inputString))

inputString = "53.5e93"
print(inputString)
print(isValidNumber(inputString))
