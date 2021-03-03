"""A number-guessing game."""
#this is a guessing-number game, 
import random

# Put your code here
print("Hello, player !")
name=input("what's your name? ")
#print(name)
comp_number = random.randint(0,100)
#print(comp_number)



#while loop exits when the right number is guessed
try:
    guess_number = int(input("Guess a number: "))
    while comp_number !=guess_number :
        if guess_number > 100 or guess_number < 0:
            print("The number is out of range")
        elif comp_number<guess_number:
            print("Your guess is too high.")
        elif comp_number>guess_number:
            print("Your guess is too low.")
        guess_number = int(input("Guess a number? "))
    print("Hurray!!! you got the right number, cake for you!")
except ValueError:
    print("This is not a number, please enter a number")


    



