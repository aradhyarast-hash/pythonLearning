# try and except blocks are used to handle any kind of error and exception comes during the operations in our code
# a = int(input("enter the number here: "))
# print("hey")
# print(a)
try:
    a = int(input("enter the number here: "))
    print(a)
except ValueError as ve:
    print("ex1")
    print(ve)
except Exception as ex:
    print("ex2")
    print(ex)

print("end of code")