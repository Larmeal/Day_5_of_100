# การหาค่าเฉลี่ย โดยใช้ list โดยที่ไม่ใช้ Sum() and Len()

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

sum_height = 0
for height in student_heights:
    sum_height += height

len_people = 0
for number in student_heights:
    len_people += 1

print(round(sum_height / len_people))