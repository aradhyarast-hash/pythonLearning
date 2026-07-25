# walrus operator 
from typing import List, Tuple, Dict, Union

if(n := len([1,2,3,4,5,6,7])) > 3:
    print(f"the size of list elements is {n}, expected < 3")

num : int = 5
name : str = "harry"

# def sum(var1 :typeofvar1 , var2 : tyoeofvar2) -> returntypeoffunction

number : List[int] = [90,100,110,120]
person : Tuple[str, int] = ("shivam" , 345)
scores : Dict[str, int] = {"alice" : 100 , "bob" : 90}

def sum(a : int, b : int) -> int:
    return a + b
