def divisible5(n):
    if(n % 5 == 0):
        return True;
    return False;

a = [334,67,32,15,75,555]
f = list(filter(divisible5, a))
print(f)
    