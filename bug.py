def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    return sum(numbers) / len(numbers)

# Example usage (this will cause ZeroDivisionError)
data = []
average = calculate_average(data)
print(f"Average: {average}")