age = input("What is your current age?")

remaining_time = 90 - int(age)
days = remaining_time * 365
weeks = remaining_time * 52
months = remaining_time * 12

print(f"You have "+str(days)+" days, "+str(weeks)+" weeks, and "+str(months)+" months left")
