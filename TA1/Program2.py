text = input("Enter a string with digits: ")

sum = 0

for char in text:
    if char.isdigit():  
        sum += int(char)  

print("Sum of digits:", sum)