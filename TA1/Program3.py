#Nested for statement
for i in range(1, 6):
    print(" " * (6 - i), end="")  
    for j in range(1, i + 1):
        print(j, end="")  
    print()  
    
print()

#Nested while statement
num = 1

while num <= 7:
    count = 1
    
    while count <= num:
        print(num, end='')
        count += 1  
    
    print()
    
    if num == 1:
        num += 2  
    elif num == 3:
        num += 2  
    elif num == 5:
        num += 1  
    elif num == 6:
        num += 1  
    elif num == 7:
        break 