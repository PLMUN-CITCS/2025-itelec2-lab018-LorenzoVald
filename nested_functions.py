def square(num):
    """Returns the square of the given number."""
    return num * num  # Or num ** 2

def sum_of_squares(numbers):
    """Returns the sum of the squares of the numbers in the list."""
    total = sum(square(n) for n in numbers)  # Using list comprehension for efficiency
    return total

# Define the list of numbers
numbers_list = [2, 3, 4]

# Call the function and print the result
result = sum_of_squares(numbers_list)
print(f"The sum of squares is: {result}")