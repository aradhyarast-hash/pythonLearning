class programmar:
    company = "deloitte"
    def __init__(self, name, id, salary):
        self.name = name
        self.id = id
        self.salary = salary

        # we need to add self as a parameter into the function because it is related to the object of the class
    def showSalary(self):
        print("the salary is the: ", self.salary)

p = programmar("moore", 101, 1000000)
print(p.name, p.id, p.salary)
r = programmar("moore", 101, 1000000)
print(r.name, r.id, r.salary)