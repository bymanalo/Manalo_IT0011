# Get user input for the variables
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = input("Enter your age: ")

# Concatenate first name and last name for full name
full_name = first_name + " " + last_name
print("\nFull Name:", full_name)

# Slice the first three characters of the first name
sliced_name = first_name[:3]
print("Sliced Name:", sliced_name)

# Create a greeting message using string formatting
print("Greeting Message: ", end="")
greeting_message = "Hello, " + sliced_name + "! Welcome. You are " + age + " years old."
print(greeting_message)