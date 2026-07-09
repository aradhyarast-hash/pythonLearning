
# function definition
def greet(name, ending = "Thank you"):
    print(f"Good day, {name}\n Wishing you a sparkling new start of your life")
    print(ending)


# function calling
greet("enzo", "with love")


def factorial(n):
    if(n == 0 or n == 1):
        return 1
    else:
        return n*factorial(n-1)

print(factorial(6))

def f_to_c(F):
    return 5*(f-32)/9

f = int(input("enter the temperature in F: "))
print(f"{round(f_to_c(f),2)} degree C")


def pattern(n):
    if(n == 0):
        return
    print("*" * n)
    pattern(n-1)

