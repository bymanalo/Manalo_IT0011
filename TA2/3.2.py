# Get user input for first name and last name
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

# Concatenate first and last name to get full name
full_name = first_name + " " + last_name

# Display full name
print("\nFull Name:", full_name)

# Display full name in both upper and lower case
print("Full Name (Upper Case):", full_name.upper())
print("Full Name (Lower Case):", full_name.lower())

# Display the length of the full name 
print("Length of Full Name:", len(full_name))