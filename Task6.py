counter = 0
number_of_negative = 0
number_of_positive = 0
number_of_zero = 0

number = int(input("Enter Number"))
while number != -1:
	number = int(input("Enter Number"))

	if number < 0:
 		number_of_negative += 1

	elif number > 0:
		number_of_positive += 1

	elif number == 0:
		number_of_zero += 1
	counter += 1

print("number_of_negative", number_of_negative)
print("number_of_positive", number_of_positive)
print("number_of_zero", number_of_zero)	

