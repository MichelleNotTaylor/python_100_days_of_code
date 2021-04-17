# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
heights_sum = 0
total_students = 0
for height in student_heights:
  total_students += 1
  heights_sum += height

average_height = int(heights_sum/total_students)
print(f"Average height: {average_height}")





