words = ["damon", "elena", "stefan", "klaus","jeremy", "caroline","bonnie","rubekah", "alaric", "enzo","katherine", "silas","kol","finn","elijah","amara", "lexi"]

with open("day8/TVD.txt", "r") as file:
    content = file.read()
for word in words:
    content = content.replace(word, "#" * len(word))

with open("day8/TVD.txt", "w") as f:
    f.write(content)

        
