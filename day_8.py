# day8
# simple python program to predict future based on input
import random

name = input("What is your name? ")

predictions = ["Tomorrow you will be very happy.", "You are going to lose a lot of money.",
 "You will have 3 kids.", "You will become like your dad.", "I am sorry, I cannot see your future."]

print(random.choice(predictions))
