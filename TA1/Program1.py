text = input("Enter a string: ")

vowels = 0
consonants = 0
spaces = 0
others = 0

for char in text:
    if char in "aeiouAEIOU":
        vowels += 1
    elif char.isalpha():
        consonants += 1
    elif char == " ":
        spaces += 1
    else:
        others += 1

print()
print("Vowels:", vowels)
print("Consonants:", consonants)
print("Spaces:", spaces)
print("Other characters:", others)