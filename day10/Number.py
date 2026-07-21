class number:
    def __init__(self, n):
        self.n = n

    def __add__(self, num):
        return self.n + num.n 

n = number(45)
m = number(90)
print(n + m)