# NUMBER STATISTICS PROGRAM

# FUNCTION 1: CALCULATE SUM
def sum_numbers(numbers):
    return sum(numbers)


# FUNCTION 2: CALCULATE AVERAGE
def average_numbers(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)


# FUNCTION 3: CALCULATE MEDIAN AND MODE
def median_mode(numbers):
    if len(numbers) == 0:
        return None, []

    sorted_numbers = sorted(numbers)
    length = len(sorted_numbers)

    # Calculate Median
    if length % 2 == 0:
        middle1 = sorted_numbers[length // 2 - 1]
        middle2 = sorted_numbers[length // 2]
        median = (middle1 + middle2) / 2
    else:
        median = sorted_numbers[length // 2]

    # Calculate Mode
    frequency = {}

    for number in numbers:
        frequency[number] = frequency.get(number, 0) + 1

    highest = max(frequency.values())

    if highest == 1:
        mode = "No mode"
    else:
        mode = [
            number for number, count in frequency.items()
            if count == highest
        ]

    return median, mode


# MAIN PROGRAM
print("===== NUMBER STATISTICS PROGRAM =====")

user_input = input("Enter numbers separated by spaces: ")

numbers = [float(n) for n in user_input.split()]

if len(numbers) == 0:
    print("Please enter at least one number.")
else:
    print("Numbers:", numbers)

    print("Sum:", sum_numbers(numbers))

    print("Average:", average_numbers(numbers))

    median, mode = median_mode(numbers)

    print("Median:", median)

    print("Mode:", mode)

print("===== PROGRAM COMPLETED =====")

input("Press ENTER to close the program...")
