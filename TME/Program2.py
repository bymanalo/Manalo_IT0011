from datetime import datetime  

date_input = input("Enter the date (mm/dd/yyyy): ")

if len(date_input) == 10 and date_input[2] == '/' and date_input[5] == '/':
    month = date_input[0:2]  
    day = date_input[3:5]    
    year = date_input[6:10] 

    if month.isdigit() and day.isdigit() and year.isdigit():
        date_object = datetime.strptime(date_input, "%m/%d/%Y")
        
        human_readable_date = date_object.strftime("%B %d, %Y")
        
        print("Date Output:", human_readable_date)
    else:
        print("Please make sure the month, day, and year are numbers.")
else:
    print("Invalid format. Please enter the date in mm/dd/yyyy format.")