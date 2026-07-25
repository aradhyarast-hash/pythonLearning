a = int(input("enter the number:"))
b = int(input("enter the number:"))

if(b == 0):
    raise ZeroDivisionError("b can not be 0.")
else:
    print(f"{a/b}")