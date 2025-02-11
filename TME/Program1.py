file = open('numbers.txt', 'r')
lines = file.readlines()
file.close()

for index in range(len(lines)):
    line = lines[index].strip()  
    numbers = line.split(',')     
    total_sum = sum(int(num) for num in numbers)  

    if str(total_sum) == str(total_sum)[::-1]:
        palindrome_status = "Palindrome"
    else:
        palindrome_status = "Not a palindrome"

    print(f"Line {index + 1}: {line} (sum {total_sum}) - {palindrome_status}")