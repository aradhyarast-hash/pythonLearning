name = input("enter your name: ")
print(f"good morning, {name}")

letter = '''congratultions! <|name|>
    you are selected.
    date: <|date|> '''
print(letter.replace("<|name|>", "aradhya").replace("<|date|>", "05-07-2026"))