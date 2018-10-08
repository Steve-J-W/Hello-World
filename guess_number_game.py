####
import random

n = random.randint(1,10)
print("I am thinking of a number between 1 and 10")

running = True
while running:
    guess_str = input("Take a guess ")
    guess = int(guess_str)
    # print(n)
    if  guess < n:
            print("Try a bigger number")
    elif guess > n:
        print("Try a smaller number")   
    elif guess == n:
        running = False
        print("Well done, that is right!")
else:
    print("Game Over")
#####
