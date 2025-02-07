# Get file name from user
filename = input("Enter file name: ")

print("\nReading Student Information:")

# Open and read the file
file = open(filename, 'r')
for line in file:
    print(line, end='')  
file.close()