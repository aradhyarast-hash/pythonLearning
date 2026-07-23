# multilevel inheritance 

class animal:
    pass

class pets(animal):
    pass

class dog(pets):
    @staticmethod
    def bark():
        print("bhow bhow")
    pass

d = dog()
d.bark()