def math_operations():
    while True:
        print("\nMathematical Operations Program")
        print("[D] - Divide")
        print("[E] - Exponentiation")
        print("[R] - Remainder")
        print("[F] - Summation")
        print("[Q] - Quit")
        
        choice = input("Enter your choice: ").strip().upper()
        
        
        if choice == 'Q':
            print("Thank you for using the program.")
            break
        
        if choice in ['D', 'E', 'R']:
            numbers = get_numbers(2)
            if numbers is None:
                continue
            a, b = numbers
            
            if choice == 'D':
                result = divide(a, b)
            elif choice == 'E':
                result = exponentiation(a, b)
            elif choice == 'R':
                result = remainder(a, b)
            
        elif choice == 'F':
            numbers = get_numbers(2)
            if numbers is None:
                continue
            start, end = numbers
            result = summation(start, end)
        else:
            print("Invalid choice. Please choose among the given options.")
            continue
        
        if result is not None:
            print("Result:", result)

def divide(a, b):
    if b == 0:
        print("Error. Denominator cannot be zero.")
        return None
    return a / b

def exponentiation(a, b):
    return a ** b

def remainder(a, b):
    if b == 0:
        print("Error. Denominator cannot be zero.")
        return None
    return a % b

def summation(start, end):
    if start > end:
        print("Error. The second number must be greater than the first number.")
        return None
    return sum(range(start, end + 1))

def get_numbers(count=2):
    try:
        numbers = [int(input(f"Enter number {i+1}: ")) for i in range(count)]
        return numbers
    except ValueError:
        print("Error: Please enter valid integers.")
        return None
    
if __name__ == "__main__":
    math_operations()