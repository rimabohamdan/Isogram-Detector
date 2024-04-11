word = input("Enter a word to check if it's an isogram: ").capitalize()
found_chars = set()
is_isogram = True
for char in word:
    if char in found_chars:
        is_isogram = False
        break
    found_chars.add(char)

if is_isogram:
    print(f"'{word}' is an isogram.")
else:
    print(f"'{word}' is not an isogram.")
