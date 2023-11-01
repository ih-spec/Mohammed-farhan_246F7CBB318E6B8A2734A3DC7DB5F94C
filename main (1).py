def factorial(n):
    if n == 0:
        return 1
    else:
        result = n * factorial(n - 1)
        print(f"Factorial of {n} is {result}")
        return result

# Call the function
result = factorial(5)
