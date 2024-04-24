
passes = 0 
failures = 0

result = int(input('Enter result (1 or 2 to stop): '))

while result != 1 and result != 2:
	result = int(input('Enter result (1 or 2 to stop): '))

	if result == 1:
		passes = passes + 1
	else:
		failures = failures + 1
print('Passed:', passes)
print('Failed:', failures)

if passes > 8:
	print('Bonus to instructor')