# hex_add_function5.py 
# this script is doing the addition of single nibbles without any carry-over.
hex1 = "FF01102030405060708090A0B0C0D0E0"   
hex2 = "10FFF102030405060708090A0B0C0D0E"
#output 0FF0012233445566778899AABBCCDDEE
def hex_addition_mod_16(hex1, hex2):
    result = []
    
    # Iterate over each pair of bytes
    for byte1, byte2 in zip(hex1, hex2):
        # Convert hex bytes to integers
        int1 = int(byte1, 16)
        int2 = int(byte2, 16)
        
        # Perform addition mod 16 for each pair of bytes
        sum_bytes = (int1 + int2) % 16
        
        # Convert the result to hexadecimal string and append to the list
        result.append(format(sum_bytes, 'X'))
    
    return result

result_list = hex_addition_mod_16(hex1, hex2)
print(result_list)


# Given list
my_list = result_list
alphanumeric_chars = [char for char in my_list if char.isalnum()]

# Step 2: Join the alphanumeric characters into a single string
result = ''.join(alphanumeric_chars)
# Step 3: Display the result
print(result)
with open("test_result.txt", 'w') as f:
    f.write(result)