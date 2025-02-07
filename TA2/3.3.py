# Get user input for student information
last_name = input("Enter last name: ")
first_name = input("Enter first name: ")
age = input("Enter age: ")
contact_number = input("Enter contact number: ")
course = input("Enter course: ")

# Formatted string of student information
student_info = "Last Name: {}\n" + "First Name: {}\n" + "Age: {}\n" + "Contact Number: {}\n" + "Course: {}\n\n"
writeData = student_info.format(last_name, first_name, age, contact_number, course)

# Write data to the file
filename = "students.txt"
file = open(filename, 'a')
file.write(writeData)
file.close()

# Display confirmation message
print("Student information has been saved to '" + filename + "'.")