# calculator 

class calculator:
    def __init__(self, n):
        self.num = n
# do not need to use self in static method because it is not related to any object of the class
    @staticmethod
    def greet():
        print("good morning user")
# self is required in instance method because it is related to the object of the class
    def square(self):
        print("the square is : ",self.num * self.num)

    def cube(self):
        print("the cube is : ",self.num * self.num * self.num)

    def squareroot(self):
        print("the square root is : ",self.num ** 0.5)\


aradhya = calculator(9)
aradhya.greet()
aradhya.square()
aradhya.cube()
aradhya.squareroot()