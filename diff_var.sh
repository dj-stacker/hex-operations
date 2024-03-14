# diff_var.sh
#!/bin/bash

# Define input byte values for string1 and string2
string1_byte1="19" #25 in decimal
string2_byte1="F1" # 241 in decimal
# result should be 216 in decimal or D8
# Convert hexadecimal strings to decimal
decimal1=$((16#${string1_byte1}))
decimal2=$((16#${string2_byte1}))

# Calculate the difference of byte1 from string1 and byte1 from string2
if [ $decimal2 -ge $decimal1 ]; then
    diff=$(( ($decimal2 - $decimal1) % 256 ))
else
    diff=$(( ($decimal2 - $decimal1 + 256) % 256 ))
fi

# Format the difference as a hexadecimal string
formatted_diff=$(printf "%02X" "$diff")  # Ensure the output is two digits representing a byte

# Print the result for verification
echo "Result: $formatted_diff"
