doubledSecondDigit = 0
firstDigit = 0
secondDigit =0
result = 0
sumofSingleDigits = 0
sum = 0
sumofdoubledSecondDigit = 0
sumTotal = 0


cardNumber = input("Hello, Enter card details to verify \n") 
	
	
collectingNumber =  len (cardNumber)	

if len(cardNumber) >= 13 & len(cardNumber) <= 16:

	for values in range(0, len(cardNumber), 2):	

		collectingNumber = cardNumber[0]
	
		doubledSecondDigit = collectingNumber * 2
	
		sumofdoubledSecondDigit = sumofdoubledSecondDigit + int(doubledSecondDigit)
	
		if(doubledSecondDigit >= 10): 
			while doubledSecondDigit != 0: 
				result = doubledSecondDigit % 10
				sum = sum + result
				doubledSecondDigit /= 10
	
 
	
	sumTotal = sumofdoubledSecondDigit + sum

	cardNumberFirstDigit: string  = cardNumber[0]
	cardNumberSecondDigit:string  = cardNumber[1]

		

	if (cardNumberFirstDigit == '4'):
		print("Credit card type: Visacard\n")
	
	elif(cardNumberFirstDigit == '5'): 
		print("Credit card type: Master card\n")
	
	elif(cardNumberFirstDigit == '6'): 
		print("Credit card type: Discover card\n")
	
	elif(cardNumberFirstDigit == '3' & cardNumberSecondDigit == '7'): 
		print("Credit card type: American express card\n")
	
		print("Credit card Number: " + cardNumber + "\n")

		print("Credit card Digit length: " + cardNumber.length() + "\n")

		if (sumTotal % 10 == 0): 
			println("Credit card validity status: Valid")
		else:  
			print("Credit card validity status: Invalid")

	else:
			println("Put correct number jare\nWerey wan scam me")
		

			
	
	
	

	

