import random
number = random.randint(1,10)
for i in range(0,3):
    user = int(input("guess the number : "))
    if user == number:
        print("Woooooopieeeeeee!!!")
        print(f"Correct! And the  number is {number}")
        break
if user != number:
    print(f"Incorrect! The number is {number}")
