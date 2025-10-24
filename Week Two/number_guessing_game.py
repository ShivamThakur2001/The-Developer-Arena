import random

guess_num = random.randint(1, 100)
print("Welcome to the number guessing game")
while(True):
    user_num = int(input("Enter your guess (range: 1 to 100): "))
    if(1 > user_num or user_num > 100):
        print("Your input is invalid!! Please restart the game")
        break
    elif(user_num < guess_num):
        print("Your Guess Is Low!! Try Again")
    elif(user_num > guess_num):
        print("Your Guess Is High!! Try Again")
    else:
        print(f"Your Input: {user_num}, System Guessed: {guess_num}\nCongratulation!! You guessed the right number.")
    
    
