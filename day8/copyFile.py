with open("day8/original.txt", "r") as file:
    content = file.read()
    
with open("day8/copy.py", "w") as f:
    f.write(content)

with open("day8/copy.py", "r") as file:
    text = file.read()
print(text)