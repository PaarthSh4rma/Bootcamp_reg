'''
What the code does and how does it do it?
1.    A random number is chosen from 1 to 100
2.    The user has to input their guess and guess is validated if the input is 
                                                                                i. an integer
                                                                               ii. between 1 and 100
3.    If their guess is higher/lower than the chosen number, they are notified and asked to guess again.
4.    This continues till the user guesses the number correctly.
5.    When the user guesses the number correctly, they are notified of the same and the game ends. 
'''
import random  # importing random library to chose number

correct_number = random.randint(1, 100)  # choosing random number between 1 and 100

while True:  # Infinite loop till the break statement is read
    try:  # validates user input
        guess = int(input("Enter a number between 1 and 100: "))  # user input
        if guess >= 1 and guess <= 100:  #checking for valid input
            if guess > correct_number:
                print("Guessed number is higher than answer\n")
            elif guess < correct_number:
                print("Guessed number is lower than answer\n")
            else:
                print("Well done!\nThe answer was: ", correct_number, "\n")
                break  # End of Game condition
        else:
            print("Guessed number is not between 1 and 100, try again")
    
    except ValueError: 
        print("Invalid Input, Enter an integer")  #Error Message if the input is not an integer
