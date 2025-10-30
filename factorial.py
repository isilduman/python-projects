n = int(input("Enter a number: "))

def factorial(n):
    result = 1
    for i in range(1, n+1):  # 1’den n’e kadar çarp
        result *= i
    return result

print(f"The factorial of {n} is {factorial(n)}")

