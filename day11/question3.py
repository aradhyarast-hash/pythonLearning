class employee:
    salary = 4
    increment = 2
    def show(self):
        print(f"salary is : {self.salary} ans increment is : {self.increment}")

    @property
    def salaryWithIncrement(self):
        return (self.salary + (self.salary * (self.increment/100)))


e = employee()
print(e.salaryWithIncrement)

