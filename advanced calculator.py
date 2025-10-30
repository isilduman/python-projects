import math
# We are defining the operations using functions
def calculate(a, b, operation):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "division":
        try:
            return a / b
        except ZeroDivisionError:
            return "Error: Division by zero"
    elif operation == "power":
        return a ** b
    elif operation == "sqrt":
        return math.sqrt(a)
    elif operation == "log":
        try:
            return math.log(a)
        except ValueError:
            return "Error: Log undefined for non-positive numbers."
    else:
        return "Invalid operation"

def main():
    print("=== Advanced Calculator ===")
    while True:
        print("\nOperations:") 
        print("add, subtract, multiply, division, power, sqrt, log") 
        print("Type 'exit' to quit")
        
        operation = input("Choose an operation: ").lower()
        if operation == "exit":
            print("Exiting...")
            break
        
        a = float(input("Please enter a number: "))  
        b = 0
        if operation not in ["sqrt", "log"]:
            b = float(input("Please enter a second number: "))
        
        result = calculate(a, b, operation)
        print("Result:", result)

if __name__ == "__main__":
    main()
