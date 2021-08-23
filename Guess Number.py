#code to guess the number which is guessed by computer randomly in a certain range. Let's see who wins... You or Computer

import random
print("Let's Start the game!")
computer_guess = random.randint(1,10)

my_guess = 0
comp_player = 0
count = 0

while my_guess != computer_guess or comp_player != computer_guess:
    count = count + 1
    my_guess = int(input("Enter the number:"))
    comp_player = random.randint(1,10)

    if my_guess == computer_guess:
        print("You Won the Game!")
        print("You choose the correct answer.The number is ", my_guess)
        print(f"You took {count} time to guess the right number")
    if comp_player == computer_guess:
        print("You Lose the Game!")
        print("Computer choose the correct answer.The number is ", comp_player) 
        print(f"Computer took {count} to guess the right number")   

    if my_guess > computer_guess:
        print("Please select the lower number. It is too high")

    if my_guess < computer_guess:
        print("The selected number is too low. Please choose the higher number")
    


