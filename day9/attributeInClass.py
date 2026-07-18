class myclass:
    attr = 90
    @staticmethod
    def __init__():
        print("this is a constructor")
    
c = myclass();
c.attr = 0;
print(c.attr)

# proof
print(myclass.attr)
demo = myclass();
print(demo.attr)