#!/bin/bash

# Define input byte values for string1 and string2
string1_byte1="D8"
string2_byte1="19"

# Calculate the sum of byte1 from string1 and byte1 from string2, and take the modulo 256
sum=$(( (16#${string1_byte1} + 16#${string2_byte1}) % 256 ))

# Format the sum as a hexadecimal string
formatted_sum=$(printf "%02X" "$sum")  # Ensure the output is two digits representing a byte

# Assign the formatted sum to a new variable with a descriptive name
result_sum_hex="$formatted_sum"

# Print the result for verification
echo "Result: $result_sum_hex"
