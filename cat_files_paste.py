# cat_files_paste.py
import os
import tkinter as tk
from tkinter import filedialog, messagebox

def validate_file_contents(file_path):
    try:
        with open(file_path, 'r') as file:
            contents = file.read().strip()
            if len(contents) != 32 or not all(c in "0123456789abcdefABCDEF" for c in contents):
                return False
    except:
        return False
    return True

def browse_file_a():
    global file_a_path
    file_a_path = filedialog.askopenfilename(title="Select File A")
    if file_a_path:
        if validate_file_contents(file_a_path):
            file_a_label.config(text=f"File A: {file_a_path.split('/')[-1]}")
            with open(file_a_path, 'r') as file:
                file_a_contents.delete('1.0', tk.END)
                file_a_contents.insert(tk.END, file.read())
        else:
            messagebox.showerror("Invalid File", "File A does not contain 16 bytes of hex data.")
            file_a_path = None

def browse_file_b():
    global file_b_path
    file_b_path = filedialog.askopenfilename(title="Select File B")
    if file_b_path:
        if validate_file_contents(file_b_path):
            file_b_label.config(text=f"File B: {file_b_path.split('/')[-1]}")
            with open(file_b_path, 'r') as file:
                file_b_contents.delete('1.0', tk.END)
                file_b_contents.insert(tk.END, file.read())
        else:
            messagebox.showerror("Invalid File", "File B does not contain 16 bytes of hex data.")
            file_b_path = None

def reverse_order():
    global file_a_path, file_b_path
    file_a_path, file_b_path = file_b_path, file_a_path
    file_a_label.config(text=f"File A: {file_a_path.split('/')[-1]}")
    file_b_label.config(text=f"File B: {file_b_path.split('/')[-1]}")

def reverse_file_a():
    contents = file_a_contents.get('1.0', tk.END)
    reversed_contents = contents[::-1]
    file_a_contents.delete('1.0', tk.END)
    file_a_contents.insert(tk.END, reversed_contents)

def reverse_file_b():
    contents = file_b_contents.get('1.0', tk.END)
    reversed_contents = contents[::-1]
    file_b_contents.delete('1.0', tk.END)
    file_b_contents.insert(tk.END, reversed_contents)

def save_concatenated_file():
    if not file_a_path or not file_b_path:
        messagebox.showerror("Error", "Please select both files before saving.")
        return

    if not os.path.exists("result_out"):
        os.makedirs("result_out")

    file_a_name = os.path.splitext(file_a_path.split('/')[-1])[0]
    file_b_name = os.path.splitext(file_b_path.split('/')[-1])[0]

    file_a_contents_str = file_a_contents.get('1.0', tk.END).replace('\n', '').strip()
    file_b_contents_str = file_b_contents.get('1.0', tk.END).replace('\n', '').strip()

    file_a_reversed = "_r" if file_a_contents_str != file_a_contents_str[::-1] else ""
    file_b_reversed = "_r" if file_b_contents_str != file_b_contents_str[::-1] else ""

    output_filename = f"{file_a_name}{file_a_reversed}_cat_{file_b_name}{file_b_reversed}.txt"
    output_path = os.path.join("result_out", output_filename)

    concatenated_contents = file_a_contents_str + file_b_contents_str

    with open(output_path, 'w') as output_file:
        output_file.write(concatenated_contents)
    messagebox.showinfo("Success", f"Concatenated file saved as {output_path}")

def create_gui():
    global root, file_a_label, file_b_label, file_a_contents, file_b_contents

    root = tk.Tk()
    root.title("File Concatenator")

    file_a_label = tk.Label(root, text="File A: ")
    file_a_label.grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)

    file_b_label = tk.Label(root, text="File B: ")
    file_b_label.grid(row=1, column=0, sticky=tk.W, padx=10, pady=5)

    browse_file_a_button = tk.Button(root, text="Browse File A", command=browse_file_a)
    browse_file_a_button.grid(row=0, column=1, padx=5, pady=5)

    browse_file_b_button = tk.Button(root, text="Browse File B", command=browse_file_b)
    browse_file_b_button.grid(row=1, column=1, padx=5, pady=5)

    reverse_order_button = tk.Button(root, text="Reverse Order", command=reverse_order)
    reverse_order_button.grid(row=2, column=0, padx=5, pady=5)

    reverse_file_a_button = tk.Button(root, text="Reverse File A", command=reverse_file_a)
    reverse_file_a_button.grid(row=2, column=1, padx=5, pady=5)

    reverse_file_b_button = tk.Button(root, text="Reverse File B", command=reverse_file_b)
    reverse_file_b_button.grid(row=2, column=2, padx=5, pady=5)

    file_a_contents = tk.Text(root, height=10, width=40)
    file_a_contents.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    file_b_contents = tk.Text(root, height=10, width=40)
    file_b_contents.grid(row=3, column=2, columnspan=2, padx=10, pady=10)

    save_button = tk.Button(root, text="Save Concatenated File", command=save_concatenated_file)
    save_button.grid(row=4, column=1, padx=5, pady=5)

    root.mainloop()

if __name__ == "__main__":
    create_gui()