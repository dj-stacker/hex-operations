import os
import random
import string

# Define the input folder paths
folder_a = 'folder_C'
folder_b = 'folder_D'

# Define the output folder path
output_folder = 'byte_sub'

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Function to subtract two hex strings byte-wise with modulo 256
def subtract_hex_bytes(hex1, hex2):
    result = []
    for i in range(0, len(hex1), 2):
        byte1 = int(hex1[i:i+2], 16)
        byte2 = int(hex2[i:i+2], 16)
        diff_bytes = (byte1 - byte2 + 256) % 256
        result.append('{:02X}'.format(diff_bytes))
    return ''.join(result)

# Find the input files in the respective folders
file_a = None
file_b = None
for file in os.listdir(folder_a):
    file_a = os.path.join(folder_a, file)
for file in os.listdir(folder_b):
    file_b = os.path.join(folder_b, file)

# Read the input files
if file_a and file_b:
    with open(file_a, 'r') as f:
        hex1 = f.read().strip()
    with open(file_b, 'r') as f:
        hex2 = f.read().strip()

    # Ensure both input files have the same length
    if len(hex1) != len(hex2):
        print("Input files have different lengths. Please ensure they are both 16 bytes.")
    else:
        # Subtract the hex strings byte-wise
        result = subtract_hex_bytes(hex1, hex2)

        # Generate a unique output filename
        random_str = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        output_filename = os.path.join(output_folder, f"{os.path.basename(file_a)}_{os.path.basename(file_b)}_{random_str}.txt")

        # Write the result to the output file
        with open(output_filename, 'w') as f:
            f.write(result)

        print(f"Output file generated: {output_filename}")
else:
    print("Input files not found in the specified folders.")