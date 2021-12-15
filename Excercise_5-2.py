# การหาค่าสูงสุดใน list โดยไม่ใช่ค่า Max

student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

student = 0
for height in student_scores:
   if height > student:
       student = height
print(f"The highest score in the class is: {student}")