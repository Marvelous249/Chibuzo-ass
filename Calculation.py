import math

principalAmount = int(input("Enter the principal amount:  "))

Annualrate = int(input("Enter the annual intrest rate:  "))

numberofYears = int(input("Enter the duration in year:  "))

NoOfMonthInYears = 12 * numberofYears

rate = Annualrate / 100

MonthlyRate = rate / 12 

monthbase = 1 + MonthlyRate

base = monthbase ** NoOfMonthInYears

num1 = principalAmount * MonthlyRate
num2 = base - 1

Monthlypayment = num1 * base / num2

print(f'${Monthlypayment:,.2f}')