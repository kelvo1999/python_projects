# this version is for a graphical user interface used tkinter for GUI
import tkinter as tk
from tkinter import messagebox

def create_gui_calculator():
    def calculate():
        try:
            num1 = float(entry_num1.get())
            num2 = float(entry_num2.get())
            operation = operation_var.get()
            
            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '%':
                result = num1 % num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                if num2 == 0:
                    messagebox.showerror("Error", "Cannot divide by zero!")
                    return
                result = num1 / num2
            else:
                messagebox.showerror("Error", "Invalid operation")
                return
                
            result_label.config(text=f"Result: {result}")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers!")
    
    # Create main window
    root = tk.Tk()
    root.title("Simple Calculator")
    
    # Create widgets
    label_num1 = tk.Label(root, text="First Number:")
    entry_num1 = tk.Entry(root)
    
    label_num2 = tk.Label(root, text="Second Number:")
    entry_num2 = tk.Entry(root)
    
    operation_var = tk.StringVar(value='+')
    operations = ['+', '-', '*', '/', '%']
    
    operation_frame = tk.Frame(root)
    for op in operations:
        rb = tk.Radiobutton(operation_frame, text=op, variable=operation_var, value=op)
        rb.pack(side=tk.LEFT)
    
    calculate_btn = tk.Button(root, text="Calculate", command=calculate)
    result_label = tk.Label(root, text="Result: ")
    
    # Layout widgets
    label_num1.grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)
    entry_num1.grid(row=0, column=1, padx=5, pady=5)
    
    label_num2.grid(row=1, column=0, padx=5, pady=5, sticky=tk.E)
    entry_num2.grid(row=1, column=1, padx=5, pady=5)
    
    operation_frame.grid(row=2, columnspan=2, pady=5)
    calculate_btn.grid(row=3, columnspan=2, pady=10)
    result_label.grid(row=4, columnspan=2)
    
    # Run the application
    root.mainloop()

# Run the GUI calculator
create_gui_calculator()