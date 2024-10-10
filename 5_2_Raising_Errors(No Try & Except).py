'''
Baahir's Repository link - https://github.com/Baahir2007/GCIS.git
Hishaam's Repository link - https://github.com/hb7464/hb7464 
Munzir's Repository link - https://github.com/munzir1910/GCIS123 
'''

import random

'''A collection of examples of 
raising errors 
'''

def guessing_game():
    
    '''A function designed to ask the user to guess a number
    and has checks to ensure the user has entered a valid 
    number as per the requirements
    '''

    answer = random.randint(1,10)       #Getting a random number from 1-10 and storing it
    num = int(input("Please enter a number between 1 and 10: "))
    
    if num < 1 or num > 10:             #Checking if the user entered a number outside the range
        raise ValueError("Invalid Guess")
    
    elif num == answer:
        print("Congrats you guess right!")
    
    else:
        print(f"Unlucky, incorrect guess, the correct answer was {answer}") #Formatting

def password_func():

    '''A function to let the user set a 
    password with the required parameters'''

    passwd = input("Enter a password between 10-20 characters long: ")
    if len(passwd) < 10 or len(passwd) > 20:
        raise ValueError("Invalid Password")
    else:
        confirm_passwd = input("Please confirm your password: ")
    if passwd != confirm_passwd:
        raise ValueError("Passwords do not match")
    
    else:
        return passwd
        

def division():

    # A function to accept two numbers and divide them
    
    num1 = int(input("Enter the numerator: "))
    num2 = int(input("Enter the denominator: "))
    
    if num2 == 0:
        raise ZeroDivisionError("Denominator cannot be 0.")
    
    print('The quotient is',num1/num2)

def main():
    #guessing_game()
    #password_func()
    division()

if __name__ == '__main__':
    main()