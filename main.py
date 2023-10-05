# main.py
import tkinter as tk
from tkinter import filedialog
from convert_files import convert_multiple_files
from convert_excel import convert_csv_to_xlsx  # Import the function from convert_excel.py

def choose_input_directory():
    input_dir = filedialog.askdirectory()
    input_var.set(input_dir)

def choose_output_directory():
    output_dir = filedialog.askdirectory()
    output_var.set(output_dir)

def convert_files():
    input_directory = input_var.get()
    output_directory = output_var.get()
    convert_multiple_files(input_directory, output_directory)

def convert_to_xlsx():
    input_directory = input_var.get()
    output_directory = output_var.get()
    convert_csv_to_xlsx(input_directory, output_directory)  # Call the function from convert_excel.py

# Create the main application window
app = tk.Tk()
app.title("EDF to CSV Converter")

# Create input directory label and entry field
input_label = tk.Label(app, text="Input Directory:")
input_label.pack()
input_var = tk.StringVar()
input_entry = tk.Entry(app, textvariable=input_var)
input_entry.pack()
input_button = tk.Button(app, text="Browse", command=choose_input_directory)
input_button.pack()

# Create output directory label and entry field
output_label = tk.Label(app, text="Output Directory:")
output_label.pack()
output_var = tk.StringVar()
output_entry = tk.Entry(app, textvariable=output_var)
output_entry.pack()
output_button = tk.Button(app, text="Browse", command=choose_output_directory)
output_button.pack()

# Create the Convert Files button
convert_button = tk.Button(app, text="Convert Files", command=convert_files)
convert_button.pack()

# Create the Convert CSV to XLSX button
convert_to_xlsx_button = tk.Button(app, text="Convert CSV to XLSX", command=convert_to_xlsx)
convert_to_xlsx_button.pack()

# Start the main event loop
app.mainloop()