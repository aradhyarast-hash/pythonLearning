import random

with open("day7/game.txt") as file:
    content = file.read();
    if(content != ""):
        yourscore = int(content)
    else:
        yourscore = 0
    compScore = random.randint(1,70)
    print(f"the score is : {compScore}")
    if(compScore > yourscore):
        with open("day7/game.txt", "w") as f:
            f.write(str(compScore))



    
    