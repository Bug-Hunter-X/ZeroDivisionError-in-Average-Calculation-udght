def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    return sum(numbers) / len(numbers)

# Example usage (demonstrates robust error handling)
data = []
average = calculate_average(data)
print(f"Average: {average}")
data = [10, 20, 30]
average = calculate_average(data)
print(f"Average: {average}") 