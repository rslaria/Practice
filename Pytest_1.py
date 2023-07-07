# Calculator program for Python

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

# Perform calculations
add = a + b
subt = a - b
mult = a * b
div = a / b
# Note b is equal to zero. The division can't work.
# Check if b is not equal to zero to avoid division by zero error
# if b != 0:
    # division = a / b
# else:
    # division = "Error: Cannot divide by zero"

# Display the results
print("Addition:", add)
print("Subtraction:", subt)
print("Multiplication:", mult)
print("Division:", div)

# input for finding the maximum
c = float(input("Enter the third number: "))

# Find the maximum value
max = max(a, b, c)

# Display the maximum value
print("Maximum value:", max)
