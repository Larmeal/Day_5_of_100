# คำนวณผลบบวกเลขตั้งแต่ 1-100 โดยมีระยะห่างเท่ากับ 2 โดยเริ่มที่ 2 และจบที่ 100

total = 0
for number in range(2, 101, 2):
    total += number
print(total)