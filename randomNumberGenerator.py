import random

min = int(input("Welcome to Angela's Random Number Generator.\nEnter your range.\nMin: "))
max = int(input("Max: "))

randomNumber = random.randint(min, max)
print("The random number is %d" % randomNumber)