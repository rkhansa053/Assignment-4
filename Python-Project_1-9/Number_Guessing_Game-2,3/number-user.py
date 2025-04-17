import random

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

print(computer_game)

