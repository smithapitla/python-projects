student_heights = input("Input a list of student heights ").split()
numerator = 0
denominator = len(student_heights)
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
  numerator = numerator + student_heights[n]

average = round(numerator/denominator)
print(average)
