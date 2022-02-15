highest_score = 0
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
  if(student_scores[n] > highest_score):
      highest_score = student_scores[n]

print(student_scores)
print(f"The highest score in the class is: "+str(highest_score))
