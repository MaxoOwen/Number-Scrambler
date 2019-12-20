import random
number = input("Enter numbers ")
n = 0
while n != len(number):
    rn = random.randint(0,9)
    n += 1
    print(rn)
