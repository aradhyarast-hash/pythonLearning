# a -> for append
# r -> for read
# w -> for write

f = open("day7/file.txt", "a")
#this appends the data to the existing data of the file.txt file
f.write("hello brother!\n")
f.close()