# we can read the file using the with statement. The advantage of using the with statement is that it automatically takes care of closing the file after we are done with it. This is important because if we forget to close the file, it can lead to memory leaks and other issues.

with open("day7/file.txt", "r") as file:
    content2 = file.readline()
    print(content2)
    content = file.read()
    print(content)
    content1 = file.readline()
    print(content1)
    content1 = file.readline()
    print(content1)
    content1 = file.readline()
    print(content1)
    # content1 = file.readlines()
    # print(content1)
    
with open("day7/file.txt", "r") as f:
    c = f.readline()
    print(c)
    c = f.readline()
    print(c)
    c = f.readline()
    print(c)
