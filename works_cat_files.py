# claude-gpt-4_cat_files2.py
import tkinter as tk
from tkinter import filedialog, scrolledtext

class FileConcatenatorApp:
    def __init__(self, master):
        self.master = master
        master.title("File Concatenator")
        master.geometry("670x400")
        master['bg'] = '#def8fc'

        # Variables
        self.file_path_a = ""
        self.file_path_b = ""
        self.text_a = ""
        self.text_b = ""
        self.order_reversed = False

        # GUI Widgets
        self.button_select_file_a = tk.Button(master, text="Select File A", command=lambda: self.load_file('A'))
        self.button_select_file_a.pack()
        self.label_file_a = tk.Label(master, text="No file selected for A")
        self.label_file_a.pack()
        self.text_area_a = scrolledtext.ScrolledText(master, height=5)
        self.text_area_a.pack()

        self.button_select_file_b = tk.Button(master, text="Select File B", command=lambda: self.load_file('B'))
        self.button_select_file_b.pack()
        self.label_file_b = tk.Label(master, text="No file selected for B")
        self.label_file_b.pack()
        self.text_area_b = scrolledtext.ScrolledText(master, height=5)
        self.text_area_b.pack()

        self.button_reverse_a = tk.Button(master, text="Reverse Text A", command=lambda: self.reverse_text('A'))
        self.button_reverse_a.pack()
        self.button_reverse_b = tk.Button(master, text="Reverse Text B", command=lambda: self.reverse_text('B'))
        self.button_reverse_b.pack()
        self.button_switch_order = tk.Button(master, text="Switch Order", command=self.switch_order)
        self.button_switch_order.pack()
        self.button_save = tk.Button(master, text="Save Concatenated File", command=self.save_file)
        self.button_save.pack()

    def load_file(self, file_label):
        file_path = filedialog.askopenfilename()
        if file_path:
            if file_label == 'A':
                self.file_path_a = file_path
                self.label_file_a.config(text=file_path)
                self.load_file_content(file_path, 'A')
            else:
                self.file_path_b = file_path
                self.label_file_b.config(text=file_path)
                self.load_file_content(file_path, 'B')

    def load_file_content(self, file_path, file_label):
        try:
            with open(file_path, 'r') as file:
                content = file.read(32)
            self.update_text_area(content, file_label)
        except Exception as e:
            print(f"Error reading file: {e}")

    def update_text_area(self, content, file_label):
        if file_label == 'A':
            self.text_area_a.delete('1.0', tk.END)
            self.text_area_a.insert(tk.END, content)
            self.text_a = content
        else:
            self.text_area_b.delete('1.0', tk.END)
            self.text_area_b.insert(tk.END, content)
            self.text_b = content

    def reverse_text(self, file_label):
        if file_label == 'A':
            self.text_a = self.text_a[::-1]
            self.text_area_a.delete('1.0', tk.END)
            self.text_area_a.insert(tk.END, self.text_a)
            self.text_a_reversed = not getattr(self, 'text_a_reversed', False)
        else:
            self.text_b = self.text_b[::-1]
            self.text_area_b.delete('1.0', tk.END)
            self.text_area_b.insert(tk.END, self.text_b)
            self.text_b_reversed = not getattr(self, 'text_b_reversed', False)
        
    def generate_filename(self):
        # Extracts filenames without extension
        name_a = self.file_path_a.split('/')[-1].split('.')[0]
        name_b = self.file_path_b.split('/')[-1].split('.')[0]

        # Check if text was reversed for file A
        text_a_reversed = getattr(self, 'text_a_reversed', False)
        name_a_suffix = "_rev" if text_a_reversed else ""

        # Check if text was reversed for file B
        text_b_reversed = getattr(self, 'text_b_reversed', False)
        name_b_suffix = "_rev" if text_b_reversed else ""

        if not self.order_reversed:
            return f"{name_a}{name_a_suffix}_cat_{name_b}{name_b_suffix}.txt"
        else:
            return f"{name_b}{name_b_suffix}_cat_{name_a}{name_a_suffix}.txt"
        
    def switch_order(self):
        self.order_reversed = not self.order_reversed
        self.text_a, self.text_b = self.text_b, self.text_a
        self.file_path_a, self.file_path_b = self.file_path_b, self.file_path_a

        # Update GUI
        self.label_file_a.config(text=self.file_path_a)
        self.label_file_b.config(text=self.file_path_b)
        self.update_text_area(self.text_a, 'A')
        self.update_text_area(self.text_b, 'B')

    def save_file(self):
        concatenated_text = self.text_a + self.text_b if not self.order_reversed else self.text_b + self.text_a
        default_filename = self.generate_filename()
        save_path = filedialog.asksaveasfilename(initialfile=default_filename)
        if save_path:
            try:
                with open(save_path, 'w') as file:
                    file.write(concatenated_text)
                print(f"File saved: {save_path}")
            except Exception as e:
                print(f"Error saving file: {e}")
    def generate_filename(self):
        # Extracts filenames without extension
        name_a = self.file_path_a.split('/')[-1].split('.')[0]
        name_b = self.file_path_b.split('/')[-1].split('.')[0]

        # Check if text was reversed for file A
        text_a_reversed = hasattr(self, 'text_a_reversed') and self.text_a_reversed
        name_a_suffix = "_rev" if text_a_reversed else ""

        # Check if text was reversed for file B
        text_b_reversed = hasattr(self, 'text_b_reversed') and self.text_b_reversed
        name_b_suffix = "_rev" if text_b_reversed else ""

        if not self.order_reversed:
            return f"{name_a}{name_a_suffix}_cat_{name_b}{name_b_suffix}.txt"
        else:
            return f"{name_b}{name_b_suffix}_cat_{name_a}{name_a_suffix}.txt"

if __name__ == "__main__":
    root = tk.Tk()
    app = FileConcatenatorApp(root)
    root.mainloop()