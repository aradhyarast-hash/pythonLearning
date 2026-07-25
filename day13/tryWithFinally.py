
def main():
    try:
        a = int(input("enter the number here: "))
        print(a)
        return 

    except ValueError as ve:
        print(ve)
        return 

    except Exception as ex:
        print(ex)
        return 
    
    else:
        print("hello its else")

    finally:
        print("                              this statement always get executed no matter if try block executes or the except block executes")
    # print("without finally")

main() 
