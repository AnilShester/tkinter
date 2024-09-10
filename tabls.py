import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry('600x500')
window.title("Tabs in Tkinter")

# notbook widget or tabs
notebook = ttk.Notebook(window)

tab1 = ttk.Frame(notebook)
label1 = ttk.Label(tab1, text="text in tab 1")
label1.pack()
button1 = ttk.Button(tab1, text="Button in tab 1")
button1.pack()

tab2 = ttk.Frame(notebook)
label2 = ttk.Label(tab2, text="Label in tab 2")
label2.pack()
entry2= ttk.Entry(tab2)
entry2.pack()

notebook.add(tab1, text= 'tab 1')
notebook.add(tab2, text= 'tab 2')

notebook.pack()


window.mainloop()
