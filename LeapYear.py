'''
Created on Jan 31, 2022

@author: joshuasapirstein
'''

year = input("Enter in the year: ")

if (year % 4 == 0):
    if (year % 100 == 0):
        if (year % 400 == 0):
            print("The year " + str(year) + " is a leap year")
        else:
            print("The year " + str(year) + " is not a leap year")
    else:
        print("The year " + str(year) + " is a leap year")
else:
    print("The year " + str(year) + " is not a leap year")
            
        

