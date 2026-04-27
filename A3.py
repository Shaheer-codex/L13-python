def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"
    
print("a. add b. subtract c. multiply d. divide")
ch = input("Enter your choice: ")

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

if ch == 'a':
    print("Result:", add(n1, n2))
elif ch == 'b':
    print("Result:", subtract(n1, n2))
elif ch == 'c':
    print("Result:", multiply(n1, n2))
elif ch == 'd':
    print("Result:", divide(n1, n2))
else:
    print("Invalid choice")