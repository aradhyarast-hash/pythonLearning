file = open("day7/file.txt", "r")
l = file.readline() #this function will return only 1st line in the file exists.
l1 = file.readline()
l2 = file.readline()
# type of l in readline function is string.
print(l, type(l))
print(l1, type(l1))
print(l2, type(l2))
# this function leaves the cursor at the end of the line, so if we call it again it will return the next line.
li = file.readlines()
print(li, type(li)) #this function will return all the lines in the file exists.

file.close()