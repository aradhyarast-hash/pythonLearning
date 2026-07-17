with open("day8/findPython.txt", "r") as file:
    lines = file.readlines()
    lineNo = 1;

for line in lines:
    if("python" in line.lower()):
        print("the line number is : ", lineNo)
        print(line)
    lineNo += 1