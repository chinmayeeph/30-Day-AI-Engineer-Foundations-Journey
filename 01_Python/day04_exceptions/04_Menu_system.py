# Create arithmetic functions as requested by constraints
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def main():
    while True:
        # 1. Print menu inside the loop so it repeats
        print("\n===== MENU =====")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Division")
        print("5. Exit")
        
        # 2. Use your get_int function safely for the choice
        option = get_int("Choose an option (1-5): ")
        
        # 3. Handle Exit option immediately
        if option == 5:
            print("Goodbye!")
            break  # Breaks out of the while loop
            
        # 4. Check for invalid numbers outside 1-5
        if option < 1 or option > 5:
            print("Invalid choice. Please choose a number between 1 and 5.")
            continue
            
        # 5. Get the numbers safely using get_int
        x = get_int("Enter first number: ")
        y = get_int("Enter second number: ")
        
        # 6. Perform only the selected operation
        if option == 1:
            print(f"Result: {add(x, y)}")
        elif option == 2:
            print(f"Result: {subtract(x, y)}")
        elif option == 3:
            print(f"Result: {multiply(x, y)}")
        elif option == 4:
            print(f"Result: {divide(x, y)}")

main()
