import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Tkinter variables")

# variables
string_var = tk.StringVar()
test_var = tk.StringVar(value='testing variables')


# function
def button_func():
    print(string_var.get())

# widgets
label= ttk.Label(master=window, text='label', textvariable=string_var)
label.pack()

entry = ttk.Entry(master=window, textvariable=string_var)
entry.pack()

test_label = ttk.Label(master=window, text="test label", textvariable=test_var)
test_label.pack()

name_entry = ttk.Entry(master=window, textvariable=test_var)
name_entry.pack()

username_entry = ttk.Entry(master=window, textvariable=test_var)
username_entry.pack()

button = ttk.Button(master=window, text= "Click", command=button_func)
button.pack()

window.mainloop()
