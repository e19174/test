def fibonacci(n):
    # Base case: return n if it's 0 or 1
    if n <= 1:
        return n
    else:
        # Recursive case: sum of the previous two Fibonacci numbers
        return fibonacci(n - 1) + fibonacci(n - 2)

# Test the function
terms = 10
print(f"The first {terms} terms of the Fibonacci sequence are:")
for i in range(terms):
    print(fibonacci(i), end=" ")
