from functools import reduce
l = [111,33,2,3455,1223,566,1]

def great(a, b):
    if(a > b):
        return a;
    return b;

print(reduce(great, ))