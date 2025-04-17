import random

def game(x):
    random_number = random.randint(1,x)
    game = 0
    while game != random_number:
        game = int(input(f"Guess a number between 1 and {x}: "))
        if game < random_number:
            print("Sorry, guess again. Too low")
        elif game > random_number:
            print("Sorry, guess again. Too high")

    print(f"Yay, congrats you have guessed the number {random_number}")


def computer_game(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            game = random.randint(low, high)
        else:
            game = low     
        feedback = input(f"Is {game} too high (H), too low (L), or correct (C)??").lower()
        if feedback == "h":
            high = game - 1
        elif feedback == "l":
            low = game + 1    
    print("Yay! The computer guessed your number, {game}, correctly!")


computer_game(10)
