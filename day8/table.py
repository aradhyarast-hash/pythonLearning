# this is the code to generate the tables from 2 to 20 for a 13 year old kid in separate files

def table(n):
    s = ""
    for i in range(1,11):
        s += f"{n} X {i} = {n * i}\n"
    with open(f"day8/table{n}", "w") as file:
        file.write(s);

for val in range(2, 21):
    table(val)