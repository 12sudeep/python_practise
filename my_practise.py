# import random




# def get_choices():
#     player_choice=input("Enter a choice(rock,paper,scissors: ")
#     options =["rock","paper","scissors"]
#     computer_choice= random.choice(options)
#     choices = {"player": player_choice,"computer":computer_choice}


#     return choices

# def check_win(player,computer):
#     print(f"You chose {player} ,computer chose{computer}")
#     if player==computer:
#         return "it's a tie!"

# check_win("rock","paper")

# age=20
# if age>=18:
#     print("you are an adult.")
# elif age>12:
#     print("you are a teenager.")
# elif age>1:
#     print("you are a child.")
# else:
#     print("you are a baby.")
# # a=3
# b=5
# if a!=b:
#     print("yes")

# choices = get_choices()
# print(choices)

# food=["pizza","carrots","eggs"]

# dict = {"name":"beau","color":choices}

# def greeting():
#     return "hi"
# response = greeting()


# import random

# def get_choices():
#   player_choice = input("Enter a choice (rock, paper, scissors): ")
#   options = ["rock", "paper", "scissors"]
#   computer_choice = random.choice(options)
#   choices = {"player": player_choice, "computer": computer_choice}
#   return choices

# def check_win(player, computer):
#   print(f"You chose {player}, computer chose {computer}")
#   if player == computer:
#     return "It's a tie!"
#   elif player == "rock":
#     if computer == "scissors":
#       return "Rock smashes scissors! You win!"
#     else:
#       return "Paper covers rock! You lose."
#   elif player == "paper":
#     if computer == "rock":
#       return "Paper covers rock! You win!"
#     else:
#       return "Scissors cuts paper! You lose."
#   elif player == "scissors":
#     if computer == "paper":
#       return "Scissors cuts paper! You win!"
#     else:
#       return "Rock smashes scissors! You lose."
      
# choices = get_choices()
# result = check_win(choices["player"], choices["computer"])
# print(result)





# # variable and functions


# player_choice="rock"
# computer_choice="paper"

# n=input("input:")
# l=[]
# for i in n:
#   l.append(i)
# print(l[1],l[2])


# string to list

# input = input("Enter your data: ")
# new_list = []
# stat=0
# for i ,char in enumerate(input):
#   if char=="-":
#     new_list.append(input[stat:i])
#     stat=i+1
# new_list.append(input[stat:])
# print (new_list)


# Here word[middle_index - 1:middle_index + 1] is a slice notation that returns a substring of the word starting from the (middle_index-1)th character and ending at the (middle_index+1)th character.
# So in the case of "sudeep" the middle_index = 3 , so the slice operator will return the character at 2nd and 3rd index, which are "d" and "e" respectively.

# wap to enter a string and print its two middle characters if number of character in string is even 
# and one middle character if number of characters in string are odd
# def middle_characters(word):
#     word_length = len(word)
#     if word_length % 2 == 0:
#         # word has an even number of characters
#         middle_index = word_length // 2
#         return word[middle_index - 1:middle_index + 1]
#     else:
#         # word has an odd number of characters
#         middle_index = word_length // 2
#         return word[middle_index]

# print(middle_characters("sdeep"))


# day 7
# In number theory, a magic number is a positive integer that can be expressed as the sum of two or more consecutive positive integers, each of which is greater than 1.
# Here is an example of a Python program that finds all the magic numbers in a given range:
# Copy code


# Python program that finds all the magic numbers in a given range
# def is_magic_number(n):
#     # Start with the smallest possible sum (2 + 3 = 5) and check
#     # if it is equal to the given number
#     i = 2
#     j = 3
#     current_sum = i + j
#     while current_sum <= n:
#         if current_sum == n:
#             return True
#         # If the current sum is less than the given number,
#         # increment the second number and add it to the sum
#         elif current_sum < n:
#             j += 1
#             current_sum += j
#         # If the current sum is greater than the given number,
#         # increment the first number and subtract it from the sum
#         else:
#             i += 1
#             current_sum -= i
#     return False

# def find_magic_numbers(start, end):
#     magic_numbers = []
#     for i in range(start, end + 1):
#         if is_magic_number(i):
#             magic_numbers.append(i)
#     return magic_numbers

# print(find_magic_numbers(1,100))





