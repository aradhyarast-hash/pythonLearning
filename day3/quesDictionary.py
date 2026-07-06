word = {
    "madad":"help",
    "kursi":"chair",
    "sabji":"vegetable",
    "paani":"water",
    "kapde":"clothes"
}

w = input("enter the word you want the meaning of:") 
print(word.get(w))#this gives NONE when non- familar key is input
# print(word[w])  #this gives error with non-familar key

s = set()
s.add(19)
s.add("19")
print(s)


# we can not perform this (below)

# l = {1,33,1,23,[1.3,55]}
# l[4][0] = 56
# print(l)


# because all elements are
# immutable
# hashable
# unordered
