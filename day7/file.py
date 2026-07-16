# f = open("day7/file.txt", "r")
# content = f.read()
# print(content)
# f.close()

# this overwrites the existing data of the file.txt file
s = "hello my name is enzo"
f = open("day7/file.txt", "w")
f.write(s)
f.close()  