l = [22,5,11,87,24,98]
l1 = (1,2,3,4,5,6,7)

index = 0
for item in l:
    print(f"index: {index} and element: {item}")
    index += 1

for index, item in enumerate(l):
    print(f"the index is {index} and value is {item}")

for i, item in enumerate(l1):
    print(f"the index is {i}, and value is {item}")
