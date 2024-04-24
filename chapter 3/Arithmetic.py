number = int(input("Enter number: "))
sum = 0
average = 0
product = 1
smallest = number
largest = 0
for number in range(3):
	numb = int(input("Enter number: "))

	if(number > largest):
		largest = number
	if(number < smallest):
		smallest = number
	sum = number + numb
	product *= sum
	average = sum / 2	
print(f'The sum is {sum}')
print(f'The product is {product}')
print(f'The average is {average}')
print(f'The largest is {largest}')
print(f'The smallest is {smallest}')



	
	

	