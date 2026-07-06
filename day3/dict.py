mark = {
    "isha": 90,
    "shubham": 23,
    "diya":100,
    "list":[12,19,57],
    0:"zainab"
}

# unordered
# mutable
# indexed
# no duplicate keys allowed


# accessing methods
print(mark["isha"])
print(mark["diya"])
print(mark["list"])
print(mark.items())
print(mark.keys())
print(mark.values())

# update 
mark.update({"shubham":88})

# directly access
print(mark)

# access by key
 
# INTERVIEW QUESTION>>>>>>>>>
# both these methods of accessing the value is different
# this line gives none if no key exists
print(mark.get("diya"))
# this line gives error if no key exists
print(mark["diya"])


