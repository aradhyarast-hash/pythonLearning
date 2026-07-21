class employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

class manager(employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)
        print("the constructor of manager")

m = manager("mary lou", 45000)
m.display()

