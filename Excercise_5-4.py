# ฝึกทำเกม FizzBuzz

for random in range(1, 101):
    if random % 15 == 0:
        print("FizzBuzz")
    elif random % 5 == 0:
        print("Buzz")
    elif random % 3 == 0:
        print("Fizz")
    else:
        print(random)
