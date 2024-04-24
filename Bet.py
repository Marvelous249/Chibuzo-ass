import random

LUCKY_NUMBER = random.randrange(1, 10)

number = 0

while number != LUCKY_NUMBER:

	timeNumber = int(input("Enter a number betwen 1 - 10: "))

	if timeNumber == LUCKY_NUMBER:
		print("u won !!!")
		break

	elif number < 1 or number > 10:
		print("Try again later ur papa no win")
	print()
else:
	print("failed") 


