def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

print("Division:", divide(10, 2))
print("Division by zero:", divide(10, 0))
