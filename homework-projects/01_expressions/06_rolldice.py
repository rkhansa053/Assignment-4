# Simulate rolling two dice, and prints results of each roll as well as the total.

"""
Simulate rolling two dice, and prints results of each
roll as well as the total.
"""
# Import the random library which lets us simulate random things like dice!
import random

# Number of sides on each die to roll
NUM_SIDES: int = 6

def main():
  
    die1: int = random.randint(1, NUM_SIDES)
    die2: int = random.randint(1, NUM_SIDES)
    
    total: int = die1 + die2
    
    print("Dice have", NUM_SIDES, "sides each.")
    print("First die:", die1)
    print("Second die:", die2)
    print("Total of two dice:", total)


if __name__ == '__main__':
    main()
