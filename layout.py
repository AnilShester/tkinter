import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry('600x500')
window.title("Layout")

# widgets

label1 = tk.Label(window, text= "Label 1", background= 'red')
label2 = tk.Label(window, text="layout 2", background='blue')
label3 = tk.Label(window, text="label 3", background='green')


#packs
# label1.pack(side='left', fill='both', expand=True)
# label2.pack(side='left', fill="both", expand=True)

#grid
# window.rowconfigure(0, weight = 1)
# window.columnconfigure(0, weight=1)
# window.columnconfigure(1, weight=1)
# window.columnconfigure(2, weight=2)  # 3rd column is twice as big as the other.

# label1.grid(row=0, column=0, sticky='ewns')
# label2.grid(row=0, column=2, sticky='ewns')
# label3.grid(row=0, column=1, sticky='nwes')


# place
label1.place(x=100,y=200, width=100, height=200)
label2.place(relx=0.5, rely=0.5, relwidth=0.5)

window.mainloop()