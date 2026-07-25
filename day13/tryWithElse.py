try:
    a = int(input("enter the number here: "))
    print(a)
    
except ValueError as ve:
    print(ve)

except Exception as ex:
    print(ex)

else:
    print("this block is executed if the try block is successful.")
