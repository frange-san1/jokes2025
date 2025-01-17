


# make this performance task ready for submission
# To give the user a fun experience hearing knock knock jokes

# joke = input("Do you want to hear a joke? ")
# if joke == "no":
#     print("Okay suit yourself!")
# while joke == "yes":
#     print("Great, Let's Play")
#     question = input("Do you want to hear a joke about robbers, tanks, or pencils? ")
#     if question == "robbers":
#         input("Knock Knock ")
#         input("Calder")
#         print("Calder police - I've been robbed!")
#         joke = input("Do you want to hear another joke or are you finished? ")
#     elif question == "tanks":
#         input("Knock Knock ")
#         input("Tank ")
#         input("You are welcome! ")
#         joke = input("Do you want to hear another joke or are you finished? ")
#     elif question == "pencils":
#         input("Knock Knock ")
#         input("Broken pencil ")
#         input("Nevermind, it's pointless! ")
#         joke = input("Do you want to hear another joke or are you finished? ")
# if joke == "finished":
#     rate = int(input("Please rate our game 1-10! "))
#     final_score = int(rate * 10)
#     print(str(final_score) + " percent satisfaction rate")
#     friend = input("Would you recommend this game to a friend? ")

#     if friend == "yes" or friend == "maybe":
#         print("Thanks, we appreciate it. ")
#     else:
#         print("Sorry you did not enjoy it. ")

#############################################################################################################################################################################



# make this performance task ready for submission
# To give the user a fun experience hearing knock knock jokes
# joke_list = ["robbers,", "tanks,", "or pencils"]
# name = input("What is your name? ")
# print(f"Welcome {name}! ")

# joke = (input("Do you want to hear a joke? "))
# joke2 = joke.lower()
# if joke2 == "no":
#     print("Okay suit yourself!")
# while joke2 == "yes":
#     print("Great, Let's Play")
#     question = input("Do you want to hear a joke about robbers, tanks, or pencils ")
#     question2 = question.lower()
#     if question2 == "robbers":
#         input("Knock Knock ")
#         input("Calder ")
#         print("Calder police - I've been robbed!")
#         joke2 = input("Do you want to hear another joke or are you finished? ")
        
#     elif question2 == "tanks":
#         input("Knock Knock ")
#         input("Tank ")
#         input("You are welcome! ")
#         joke2 = input("Do you want to hear another joke or are you finished? ")

#     elif question2 == "pencils":
#         input("Knock Knock ")
#         input("Broken pencil ")
#         input("Nevermind, it's pointless! ")
#         joke2 = input("Do you want to hear another joke or are you finished? ")

# if joke2 == "finished":
#     rate = int(input("Please rate our game 1-10! "))
#     final_score = int(rate * 10)
#     print(str(final_score) + " percent satisfaction rate")
#     friend = input("Would you recommend this game to a friend? ")
#     if friend == "yes" or friend == "maybe":
#         print("Thanks, we appreciate it. ")
#     else:
#         print("Sorry you did not enjoy it. ")
##################################################################################################################################################################################################################################
        




# make this performance task ready for submission
# To give the user a fun experience hearing knock knock jokes

# joke_list = ("robbers,", "tanks,", "or pencils") # List of joke options.
# name = input("What is your name? ") # Asks for User's name.
# print(f"Welcome {name}!")  # Welcomes the User.

# joke = input("Do you want to hear a joke? ")    # Asks the User if they'd like to hear a joke.
# joke = joke.lower()    # Makes "joke" input lowercase, which allows for all inputs to be recognized no matter the capitilization.

# if joke == "no":
#     print("Okay suit yourself!")
# while joke == "yes":
#     print("Great, Let's Play")
#     question = input(f"Do you want to hear a joke about {joke_list} ") # Gives the User 3 joke options to choose from
#     question = question.lower()    # Makes "question" input lowercase, which allows for all inputs to be recognized no matter the capitilization.
    
#     if question == "robbers": # Joke Option #1.
#         input("Knock Knock ")
#         input("Calder ")
#         print("Calder police - I've been robbed!")
#         joke = input("Do you want to hear another joke or are you finished? ")  # Asks the User if they'd like to listen to another joke
        
#     elif question == "tanks": # Joke Option #2.
#         input("Knock Knock ") 
#         input("Tank ")
#         print("You are welcome!")
#         joke = input("Do you want to hear another joke or are you finished? ")  # Asks the User if they'd like to listen to another joke

#     elif question == "pencils": # Joke Option #3.
#         input("Knock Knock ")
#         input("Broken pencil ")
#         print("Nevermind, it's pointless!")
#         joke = input("Do you want to hear another joke or are you finished? ")  # Asks the User if they'd like to listen to another joke


# scoring = [] # Purpose: Empty List for the User's score of the game, which allows the scoring process to have a result.
# if joke == "finished":
#     rate = int(input("Please rate our game 1-10! ")) # Asks for User's rating.
#     scoring = rate # Inputs rate into empty list, so it can go through scoring process.
#     def scoring_process(scoring): # Function for scoring process.
#         final_score = int(scoring * 10) # Uses scoring list and multiplies it by last to get final score percentage
#         return final_score
#     print(str(scoring_process(scoring)) + " percent satisfaction rate") # Prints out function result.
#     friend = input("Would you recommend this game to a friend? ") # Asks User if they would recommend this game.
#     if friend == "yes" or friend == "maybe":
#         print("Thanks, we appreciate it. ") # If YES or MAYBE, then this will display.
#     else:
#         print("Sorry you did not enjoy it. ") # If OTHER ANSWER, then this will display.



# make this performance task ready for submission
# To give the user a fun experience hearing knock knock jokes

joke_list = ["robbers,", "tanks,", "or pencils"] # List of joke options.
name = input("What is your name? ") # Asks for User's name.
print(f"Welcome {name}!")  # Welcomes the User.

joke = input("Do you want to hear a joke? ")    # Asks the User if they'd like to hear a joke.
joke = joke.lower() # Makes "joke" input lowercase, which allows for all inputs to be recognized no matter the capitilization.

if joke == "no":
    print("Okay suit yourself!")
while joke == "yes":
    print("Great, Let's Play")
    question = input("Do you want to hear a joke about robbers, tanks, or pencils? ") # Gives the User 3 joke options to choose from
    question = question.lower() # Makes "question" input lowercase, which allows for all inputs to be recognized no matter the capitilization.
    for jokes in joke_list:
        if question == "robbers": # Joke Option #1.
            input("Knock Knock ")
            input("Calder ")
            print("Calder police - I've been robbed!")
            joke = input("Do you want to hear another joke or are you finished? ")  # Asks the User if they'd like to listen to another joke
        
        elif question == "tanks": # Joke Option #2.
            input("Knock Knock ") 
            input("Tank ")
            print("You are welcome!")
            joke = input("Do you want to hear another joke or are you finished? ")  # Asks the User if they'd like to listen to another joke

        elif question == "pencils": # Joke Option #3.
            input("Knock Knock ")
            input("Broken pencil ")
            print("Nevermind, it's pointless!")
            joke = input("Do you want to hear another joke or are you finished? ")  # Asks the User if they'd like to listen to another joke


scoring = [] # Purpose: Empty List for the User's score of the game, which allows the scoring process to have a result.
if joke == "finished":
    rate = int(input("Please rate our game 1-10! ")) # Asks for User's rating.
    scoring = rate # Inputs rate into empty list, so it can go through scoring process.
    def scoring_process(scoring): # Function for scoring process.
        final_score = int(scoring * 10) # Uses scoring list and multiplies it by last to get final score percentage
        return final_score
    result = str(scoring_process(scoring))
    print((result) + " percent satisfaction rate")# Prints out function result.
    if int(result) > 70:
        friend = input("Glad to hear you enjoyed the game! Would you recommend this game to a friend? ") # Asks User if they would recommend this game.
    else:
        unfortunate = input("Sad to hear that you didn't enjoy the game.")
    if friend == "yes" or friend == "maybe":
        print("Thanks, we appreciate it. ") # If YES or MAYBE, then this will display.
    else:
        print("That's okay. ") # If OTHER ANSWER, then this will display.
