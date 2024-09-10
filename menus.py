import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry('600x500')
window.title("Tkinter Menus")

# Menubar
menubar = tk.Menu(window)

# sub menu
file_menu = tk.Menu(menubar, tearoff=False)
file_menu.add_command(label = "New file", command = lambda: print("New file"))
file_menu.add_command(label= "Open file", command = lambda: print("Open File"))
# file_menu.add_separator()
menubar.add_cascade(label= "File", menu = file_menu)

# another sub menu
help_menu = tk.Menu(menubar, tearoff=False)
help_menu.add_command(label = "Open Help", command= lambda: print(help_check_string.get()))

help_check_string = tk.StringVar()
help_menu.add_checkbutton(label = "check", onvalue = 'on', offvalue = 'off', variable= help_check_string)  # variable sets the onvalue and off value when checked or uncheckekd 

menubar.add_cascade(label= "Help", menu = help_menu)

# adding menu bar to the window
window.config(menu = menubar)

#menu button
menu_button = ttk.Menubutton(window, text="Menu button")
menu_button.pack()

# menu button sub menus
button_sub_menu = tk.Menu(menu_button, tearoff= False)
button_sub_menu.add_command(label="entry 1", command = lambda: print("test 1"))


menu_button.configure(menu= button_sub_menu)



window.mainloop()