number = int(input("enter the number : "))
ans = [number*i for i in range(1,11)]

with open("table.txt", 'a') as f:
    f.write(str(ans) + '\n');
    print("table added!")