def calculate():
    while True:
        # Get first number
        num1 = input("Enter first number (or press Enter to quit): ")
        if num1 == "":
            print("Calculator closing...")
            break
            
        # Get operation
        operation = input("Enter operation (+, -, *, /): ")
        
        # Get second number
        num2 = input("Enter second number: ")
        
        try:
            num1 = float(num1)
            num2 = float(num2)
            
            # Perform calculation based on operation
            if operation == "+":
                result = num1 + num2
            elif operation == "-":
                result = num1 - num2
            elif operation == "*":
                result = num1 * num2
            elif operation == "/":
                if num2 == 0:
                    print("Error: Cannot divide by zero!")
                    continue
                result = num1 / num2
            else:
                print("Invalid operation!")
                continue
                
            print(f"Result: {result}")
            
        except ValueError:
            print("Please enter valid numbers!")
            continue

if __name__ == "__main__":
    print("Simple Calculator")
    print("Enter numbers and operations when prompted")
    print("Press Enter without any input to quit")
    calculate()
