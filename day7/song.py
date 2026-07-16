with open("day7/song.txt", "r") as file:
    content = file.readline()
    while(content):
        if("I want" in content):
            print(content)
        content = file.readline()
        