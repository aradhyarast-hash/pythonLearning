def func():
    print("hello world!")

# if we are executing this __name__ in the actual file in which it is present 
print(__name__)

if(__name__ == "__main__"):
    print("we are directly running this code.")
    func()
    print(__name__)
