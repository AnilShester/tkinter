import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry("600x500")
window.title("Combo and Spin")

#combobox
items = ("Ice cream", "Pizza", "Kebeb")
food_string = tk.StringVar(value= items[0])
combo = ttk.Combobox(window, textvariable= food_string)
combo.config(values= items) 
# combo['values'] = items        same as the top one
combo.pack()

#events for combo
combo.bind("<<ComboboxSelected>>", lambda event: print(food_string.get()))

# Spinbox
spin = ttk.Spinbox(window, from_=1, to=20, increment=2, command= lambda: print("arrow was clicked"))
spin.bind("<<Increment>>", lambda event: print('up'))
spin.bind("<<Decrement>>", lambda event: print("Down"))
spin.pack()


window.mainloop()
