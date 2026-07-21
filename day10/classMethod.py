class employee:
    a = 1
# encapsulation in class

    # for getting class attribute 
    @classmethod
    def show(cls):
        print(f"this is {cls.a}")

# its a  decorator
    @property
    def name(self):
        return f"{self.fname} {self.sname}"
    
# this is the abstraction concept of the oops in python 
    @name.setter
    def name(self,value):
        self.fname = value.split(" ")[0]
        self.sname = value.split(" ")[1]

emp = employee()
emp.a = 50

emp.name = "aradhya rastogi"
# instance attribute will be shown now
print(emp.name)

emp.show()