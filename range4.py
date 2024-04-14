passes = 0

failes = 0

for number in range(1,16):

	result = int(input("Enter the score"))

	if result >= 45:

		passes = passes + 1

	else:

		failes = failes + 1 


print("Excellent", passes)

		
print("failure", failes)
