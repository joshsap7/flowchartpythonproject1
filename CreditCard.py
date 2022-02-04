'''
Created on Feb 2, 2022

@author: joshuasapirstein
'''

def get_digit(number, n):
    return number // 10**n % 10

cc = input("Enter in the credit card number: ")
sum = 0
digit = 0

for x in range(12):
    if (x + 1 % 2 == 0):
        digit = get_digit(cc, x + 1)
        digit = digit * 2
        if (digit > 9):
            num1 = get_digit(digit, 1)
            num2 = get_digit(digit, 2)
            digit = num1 + num2
    
    sum += digit
    

if (sum % 10 == 0):
    print("The credit card number is valid.")
else:
    print("The credit card number is invalid.")


