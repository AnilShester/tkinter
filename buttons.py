import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Buttons")
window.geometry("600x400")

# functions
def button1_click():
    print("Button 1 Clikced")


# button
button1 = ttk.Button(window, text="Button 1", command=button1_click)
button1.pack()

# checkbutton
check_var = tk.IntVar()
check_button = ttk.Checkbutton(
    window,
    text= 'Checkbox',
    command= lambda: print(check_var.get()),
    variable=check_var,
    )
check_button.pack()

# radio buttons
radio_var = tk.StringVar()

radio1 = ttk.Radiobutton(
    window, 
    text="Option 1", 
    value='option 1',
    variable= radio_var,
    command= lambda: print(radio_var.get()))
radio1.pack()

radio2 = ttk.Radiobutton(
    window, 
    text="Option 2", 
    value= 'option 2',
    variable=radio_var,
    command= lambda: print(radio_var.get()))
    
radio2.pack()



# challange
check_btn_var = tk.BooleanVar()
check_btn = ttk.Checkbutton(
    window,
    text= "Check the box",
    variable=check_btn_var,
    command= lambda:(print(check_btn_var.get()))
)
check_btn.pack()

radio_btn_var = tk.StringVar()
radio_btn1 = ttk.Radiobutton(
    window,
    text="Radio 1",
    value= "A",
    variable=radio_btn_var,
    command= lambda: print(radio_btn_var.get())
)
radio_btn1.pack()

radio_btn2 = ttk.Radiobutton(
    window,
    text= "Radio 2",
    value="B",
    variable= radio_btn_var,
    command= lambda: print(radio_btn_var.get())
)
radio_btn2.pack()



window.mainloop()