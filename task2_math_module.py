# Task 2: Math Module Calculations

import math

# Ask the user for a number
num = float(input("Enter a number: "))

# Perform calculations
sqrt_result = math.sqrt(num)
log_result = math.log(num)
sine_result = math.sin(num)

# Display results
print(f"Square root of {num}: {sqrt_result}")
print(f"Natural logarithm of {num}: {log_result}")
print(f"Sine of {num} (in radians): {sine_result}")
