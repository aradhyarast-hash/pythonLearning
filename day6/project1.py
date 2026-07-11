# lets make a game -> SNAKE, WATER, GUN

'''
-1 snake
0 water
1 gun
'''
# impoted the random module from the python library

import random
computer = random.choice([-1,0,1])

rules = {'s' : -1, 'w' : 0, 'g' : 1}

chance = 3
c = 0
y = 0
while(chance != 0):
    yours = input("enter your choice: ")
    you = rules.get(yours)
    if(computer == -1 and you == 0):
        print(f"you chose water")
        print("computer chose snake")
        print("you lost...")
        c += 1
    elif(computer == 0 and you == -1):
        print("you chose snake")
        print("computer chose water")
        print("you won!")
        y += 1
    elif(computer == -1 and you == 1):
        print("you chose gun")
        print("computer chose snake")
        print("you won!")
        y += 1
    elif(computer == 1 and you == -1):
        print("you chose snake")
        print("computer chose gun")
        print("you lost...")
        c += 1
    elif(computer == 0 and you == 1):
        print("you chose gun")
        print("computer chose water")
        print("you lost...")
        c += 1
    elif(computer == 1 and you == 0):
        print("you chose water")
        print("computer chose gun")
        print("you won!")
        y += 1
    elif(computer == you):
        print("you both chose the same")
        print("tie...")
    else:
        print('''please select a valid choice out of
            snake -> s
            water -> w
            gun   -> g''')
        chance += 1
    chance -= 1
    

if(c > y):
    print('''Sorry, 
    You lost the game...
    better luck, next time''')

elif(c < y):
    print("Hurrah! You won the game!!!")

else:
    print('''Game tied!
    wanna try once again?
    run the code''')