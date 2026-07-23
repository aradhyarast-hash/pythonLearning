class vector_2d:

    def __init__(self, len, brd):
        self.len = len
        self.brd = brd
        print("this is the 2d vector class running.")
    
    def showProp(self):
        return f"{self.len} and {self.brd} are the two properties."
    
class vector_3d(vector_2d):
    het = 10
    def __init__(self, len , bred, het):
        super().__init__(len, bred)
        self.het = het
        print("this is the 3d vector class.")

    def showProperty(self):
        return f"and {self.het} is the property."
    

vec = vector_3d(12, 89, 90)
# vec.het = 90
# vec.brd = 20
print(vec.showProp())
print(vec.showProperty())