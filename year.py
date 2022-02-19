
def checkYear(year):
    if(year % 4 == 0):
        if(year % 100 == 0 and year % 400 == 0):
            return True
        else:
            return False
    else:
        return False


userInput = int(input("Enter the year you wish to test:"))
if (checkYear(userInput)):
    print(f'{userInput} is a leap year')

else:
    print(f'{userInput} is not a leap year')


