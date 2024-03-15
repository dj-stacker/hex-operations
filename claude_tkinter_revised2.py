import tkinter as tk
from tkinter import filedialog, simpledialog
import threading
import time
import random
import string
import os

def generate_unique_id():
    timestamp = int(time.time())
    random_chars = ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))
    return f"{timestamp}_{random_chars}"

def open_file_thread(file_type):
    filename = filedialog.askopenfilename(
        initialdir="./",
        title=f"Open File {file_type}",
        filetypes=(("Text Files", "*.txt"),)
    )

    if filename:
        with open(filename, 'r') as file:
            data = file.read()

        if file_type == "A":
            data_text_A.delete('1.0', tk.END)
            data_text_A.insert(tk.END, data)
            unique_id = generate_unique_id()
            last_files[f"Filename_1_{unique_id}"] = filename
            last_datas[f"Data_1_{unique_id}"] = data
            file_label_A.config(text=os.path.basename(filename))
            file_label_A.unbind('<Enter>')
            file_label_A.bind('<Enter>', lambda event, path=filename: show_path(path))
            print(f"File A {unique_id}", filename, data)
        elif file_type == "B":
            data_text_B.delete('1.0', tk.END)
            data_text_B.insert(tk.END, data)
            unique_id = generate_unique_id()
            last_files[f"Filename_2_{unique_id}"] = filename
            last_datas[f"Data_2_{unique_id}"] = data
            file_label_B.config(text=os.path.basename(filename))
            file_label_B.unbind('<Enter>')
            file_label_B.bind('<Enter>', lambda event, path=filename: show_path(path))
            print(f"File B {unique_id}", filename, data)

def open_file_A():
    threading.Thread(target=open_file_thread, args=("A",)).start()

def open_file_B():
    threading.Thread(target=open_file_thread, args=("B",)).start()

def handle_reverse(data_text, reversed_text):
    def reverse_thread():
        data = data_text.get('1.0', tk.END).rstrip('\n')
        reversed_data = data[::-1]
        print("Reversed data:", reversed_data)
        reversed_text.delete('1.0', tk.END)
        reversed_text.insert(tk.END, reversed_data)
        reversed_text.mark_set("insert", "1.0")

    threading.Thread(target=reverse_thread).start()

def hex_full_byte_addition_mod_256(hex1, hex2):
    assert len(hex1) == len(hex2), "Hexadecimal strings must be of the same length"
    result_hex = ""

    for i in range(0, len(hex1), 2):
        byte1 = hex1[i:i+2]
        byte2 = hex2[i:i+2]

        int1 = int(byte1, 16)
        int2 = int(byte2, 16)

        sum_bytes = (int1 + int2) % 256
        result_hex += format(sum_bytes, '02X')

    return result_hex

def hex_full_byte_subtraction_mod_256(hex1, hex2):
    assert len(hex1) == len(hex2), "Hexadecimal strings must be of the same length"
    result_hex = ""

    for i in range(0, len(hex1), 2):
        byte1 = int(hex1[i:i+2], 16)
        byte2 = int(hex2[i:i+2], 16)
        diff = (byte1 - byte2)
        if diff < 0:
            diff += 256
        result_hex += format(diff, '02X')

    return result_hex

def hex_nibble_addition_mod_16(hex1, hex2):
    assert len(hex1) == len(hex2), "Hexadecimal strings must be of the same length"
    result_hex = ""

    for i in range(0, len(hex1), 2):
        byte1 = hex1[i:i+2]
        byte2 = hex2[i:i+2]

        nibble1_1 = int(byte1[0], 16)
        nibble1_2 = int(byte1[1], 16)
        nibble2_1 = int(byte2[0], 16)
        nibble2_2 = int(byte2[1], 16)

        sum_nibble1 = (nibble1_1 + nibble2_1) % 16
        sum_nibble2 = (nibble1_2 + nibble2_2) % 16

        result_hex += format(sum_nibble1, 'X') + format(sum_nibble2, 'X')

    return result_hex

def hex_nibble_subtraction_mod_16(hex1, hex2):
    assert len(hex1) == len(hex2), "Hexadecimal strings must be of the same length"
    result_hex = ""

    for i in range(0, len(hex1), 2):
        byte1 = hex1[i:i+2]
        byte2 = hex2[i:i+2]

        nibble1_1 = int(byte1[0], 16)
        nibble1_2 = int(byte1[1], 16)
        nibble2_1 = int(byte2[0], 16)
        nibble2_2 = int(byte2[1], 16)

        diff_nibble1 = (nibble1_1 - nibble2_1 + 16) % 16
        diff_nibble2 = (nibble1_2 - nibble2_2 + 16) % 16

        result_hex += format(diff_nibble1, 'X') + format(diff_nibble2, 'X')

    return result_hex

def hex_xor(hex1, hex2):
    assert len(hex1) == len(hex2), "Hexadecimal strings must be of the same length"
    result_hex = ""

    for i in range(0, len(hex1), 2):
        byte1 = hex1[i:i+2]
        byte2 = hex2[i:i+2]

        int1 = int(byte1, 16)
        int2 = int(byte2, 16)

        xor_result = int1 ^ int2
        result_hex += format(xor_result, '02X')

    return result_hex

def show_path(path):
    path_label.config(text=path)
    path_label.after(2000, lambda: path_label.config(text=""))

def perform_operation(operation):
    input_A = input_option_A.get()
    input_B = input_option_B.get()

    if input_A == "File A":
        data_A = data_text_A.get('1.0', tk.END).rstrip('\n')
    elif input_A == "Reversed A":
        data_A = reversed_text_A.get('1.0', tk.END).rstrip('\n')

    if input_B == "File B":
        data_B = data_text_B.get('1.0', tk.END).rstrip('\n')
    elif input_B == "Reversed B":
        data_B = reversed_text_B.get('1.0', tk.END).rstrip('\n')

    if operation == "Byte Addition (Mod 256)":
        result = hex_full_byte_addition_mod_256(data_A, data_B)
    elif operation == "Byte Subtraction (Mod 256)":
        result = hex_full_byte_subtraction_mod_256(data_A, data_B)
    elif operation == "Nibble Addition (Mod 16)":
        result = hex_nibble_addition_mod_16(data_A, data_B)
    elif operation == "Nibble Subtraction (Mod 16)":
        result = hex_nibble_subtraction_mod_16(data_A, data_B)
    elif operation == "XOR":
        result = hex_xor(data_A, data_B)

    result_text.delete('1.0', tk.END)
    result_text.insert(tk.END, result)

    history_text.insert(tk.END, f"{operation} ({input_A}, {input_B}):\n{result}\n\n")
    history_text.see(tk.END)

def handle_reverse_result():
    handle_reverse(result_text, result_text)

def save_result():
    filename = filedialog.asksaveasfilename(defaultextension=".txt")
    if filename:
        with open(filename, 'w') as file:
            file.write(result_text.get('1.0', tk.END))

root = tk.Tk()
root.title("Hex Operations- Claude Tk Revised 2")
root.geometry("970x600")
root['bg'] = '#def8fc'

last_files = {}
last_datas = {}

permanent_frame = tk.Frame(root)
permanent_frame.pack(side=tk.LEFT, fill=tk.BOTH, padx=10, pady=10)

file_frame_A = tk.Frame(permanent_frame)
file_frame_A.pack(side=tk.TOP, pady=10)
file_label_A = tk.Label(file_frame_A, text="File A", width=10)
file_label_A.pack(side=tk.LEFT, padx=10)
data_text_A = tk.Text(file_frame_A, width=40, height=5)
data_text_A.pack(side=tk.LEFT, padx=10)
tk.Button(file_frame_A, text="Open", command=open_file_A).pack(side=tk.LEFT, padx=10)

file_frame_B = tk.Frame(permanent_frame)
file_frame_B.pack(side=tk.TOP, pady=10)
file_label_B = tk.Label(file_frame_B, text="File B", width=10)
file_label_B.pack(side=tk.LEFT, padx=10)
data_text_B = tk.Text(file_frame_B, width=40, height=5)
data_text_B.pack(side=tk.LEFT, padx=10)
tk.Button(file_frame_B, text="Open", command=open_file_B).pack(side=tk.LEFT, padx=10)

reversed_frame_A = tk.Frame(permanent_frame)
reversed_frame_A.pack(side=tk.TOP, pady=10)
tk.Label(reversed_frame_A, text="Reversed A:", width=10).pack(side=tk.LEFT, padx=10)
reversed_text_A = tk.Text(reversed_frame_A, width=40, height=5)
reversed_text_A.pack(side=tk.LEFT, padx=10)
tk.Button(reversed_frame_A, text="Reverse", command=lambda: handle_reverse(data_text_A, reversed_text_A)).pack(side=tk.LEFT, padx=10)

reversed_frame_B = tk.Frame(permanent_frame)
reversed_frame_B.pack(side=tk.TOP, pady=10)
tk.Label(reversed_frame_B, text="Reversed B:", width=10).pack(side=tk.LEFT, padx=10)
reversed_text_B = tk.Text(reversed_frame_B, width=40, height=5)
reversed_text_B.pack(side=tk.LEFT, padx=10)
tk.Button(reversed_frame_B, text="Reverse", command=lambda: handle_reverse(data_text_B, reversed_text_B)).pack(side=tk.LEFT, padx=10)

selectable_frame = tk.Frame(root)
selectable_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

function_frame = tk.Frame(selectable_frame)
function_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=10)

input_option_A = tk.StringVar()
input_option_A.set("File A")
input_option_B = tk.StringVar()
input_option_B.set("File B")

input_frame = tk.Frame(function_frame)
input_frame.pack(side=tk.TOP, pady=10)
tk.Label(input_frame, text="Input A:").pack(side=tk.LEFT, padx=10)
input_option_menu_A = tk.OptionMenu(input_frame, input_option_A, "File A", "Reversed A")
input_option_menu_A.pack(side=tk.LEFT, padx=10)
tk.Label(input_frame, text="Input B:").pack(side=tk.LEFT, padx=10)
input_option_menu_B = tk.OptionMenu(input_frame, input_option_B, "File B", "Reversed B")
input_option_menu_B.pack(side=tk.LEFT, padx=10)

operations = [
    "Byte Addition (Mod 256)",
    "Byte Subtraction (Mod 256)",
    "Nibble Addition (Mod 16)",
    "Nibble Subtraction (Mod 16)",
    "XOR"
]
operation_menu = tk.StringVar()
operation_menu.set(operations[0])
operation_dropdown = tk.OptionMenu(function_frame, operation_menu, *operations, command=perform_operation)
operation_dropdown.pack(side=tk.TOP, padx=10, pady=10)

result_frame = tk.Frame(function_frame)
result_frame.pack(side=tk.TOP, pady=10)
tk.Label(result_frame, text="Result:").pack(side=tk.TOP, padx=10)
result_text = tk.Text(result_frame, width=40, height=15)
result_text.pack(side=tk.TOP, padx=10)
tk.Button(result_frame, text="Reverse Result", command=handle_reverse_result).pack(side=tk.TOP, padx=10)
tk.Button(result_frame, text="Save Result", command=save_result).pack(side=tk.TOP, padx=10)

history_frame = tk.Frame(selectable_frame)
history_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=10)
tk.Label(history_frame, text="History:").pack(side=tk.TOP, padx=10)
history_text = tk.Text(history_frame, width=40, height=15)
history_text.pack(side=tk.TOP, padx=10)

path_label = tk.Label(root, text="", fg="gray")
path_label.pack(side=tk.BOTTOM, pady=10)

root.mainloop()
