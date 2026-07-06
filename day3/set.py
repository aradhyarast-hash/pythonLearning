s =  {1,5,32}
# s = {} this creates an empty dictionery
e = set() #empty set
# set takes only unique values

# unordered
# unindexed
# unmutable
# no duplicate values

S = {2,5,32,1,2,2,32,"harry"}
print(S, type(S))
print(len(S))
S.remove(32)
print(S)

# union of sets
s1 = {3,1,66,1,2}
s2 = {100,19,1,66,23}

print(s1.union(s2)) #doesnot effect original s1 and s2 sets
print(s1)
print(s2)
print(s1.intersection(s2))

# it gives the elements in s1 that are not common with s2 -> difference
print(s1.difference(s2))

print({3,1}.issubset(s1))
print(s1.issuperset({1,3}))
print(s2.pop())

print(s1.clear()) #none printed
print(s1)
