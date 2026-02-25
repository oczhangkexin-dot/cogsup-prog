"""
Have a look at the script called 'human-guess-a-number.py' (in the same folder as this one).

Your task is to invert it: You should think of a number between 1 and 100, and the computer 
should be programmed to keep guessing at it until it finds the number you are thinking of.

At every step, add comments reflecting the logic of what the particular line of code is (supposed 
to be) doing. 
"""
from random import randint

def start():
    """Prompt the user to start the guessing game"""
    while True: #Repeat the prompt until the user inputs the valid answer"
        if input("Please choose a number between 1 and 100. I will try to find it! Say 'yes' to start. ") == "yes": 
            break

def ask(guess):
    """
    Outputting a number between 1 and 100 based on user's inputs. Repeat this process until the computer guesses out the correct number 
    The strategy adopted by this function allows the computer to guess out the number in fewest steps
    Argument(guess) is a randomly chosen number between 1 and 100
    """
    guess1 = 100 #the defalt lowest number that higher than the number chosen by user (lowest number for "too high")
    guess2 = 0 #the default highest number that lower than the number chosen by user (highest number for "too low")
    while True:
        p = input(f"{guess} (Is it correct, too low, or too high?) ") #prompt user to input "too low", "too high", or "correct" based on the numer that the computer guesses
        if p != "correct": 
            if p == "too low":
                guess2 = guess #updates the highest number for "too low"
                guess = int((guess1 - guess) * 1/2) + guess #calculates the midpoint between the present number and the lowest number for "too high"; turn the midpoint into an integer 
            elif p == "too high":
                guess1 = guess #updates the highest number for "too low"
                guess = guess - int((guess-guess2) * 1/2) #calculates the midpoint between the present number and the highest number for "too low"; turn the midpoint into an integer
        else: # return the number that the computer guesses if user inputs "correct"
            return guess

def main():
    guess = randint(1, 100) # Computer selects a random number between 1 and 100 inclusive
    start() # Computer outputs numbers between 1 and 100 until the number is correct
    a = ask(guess)
    print("I win! The number was indeed " + str(a))

main()