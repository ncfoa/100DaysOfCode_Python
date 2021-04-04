#heights, 48 38 60 55 63
student_heights = input("Input a list of student heights in inches ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

divide = 0
avg = 0

for student in student_heights:
    avg += student
    divide += 1

avg = round(avg / divide)

print(f"Average height is {avg} inches ")