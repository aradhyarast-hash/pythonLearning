# number guessing game
import random 
num = random.randint(1,101)
attempt = 7
won = False
while(attempt):
    a = int(input("enter your guess: "))
    if(a == num) :
        print("you guessed it right.")
        print("you won!!!")
        won = True
        break;
    elif(a < num):
        print("guess a higher number")

    else:
        print("guess a smaller number")
    attempt -= 1

if(won == False):
   print(f"the number was {num}")
   print("you lost!!!")
