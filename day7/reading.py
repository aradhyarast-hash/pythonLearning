# printing the content of the file using the while loop

f = open("day7/file.txt", "r")
line = f.readline()
while(line != ""):
    print(line)
    line = f.readline()

f.close()