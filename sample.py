# sample.py

def add(x, y):
    """Function to add two numbers."""
    return x + y

def subtract(x, y):
    """Function to subtract two numbers."""
    return x - y

def multiply(x, y):
    """Function to multiply two numbers."""
    return x * y

def divide(x, y):
    """Function to divide two numbers."""
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y

# Example usage
if __name__ == "__main__":
    print(add(5, 3))
    print(subtract(5, 3))
    print(multiply(5, 3))
    print(divide(6, 3))
