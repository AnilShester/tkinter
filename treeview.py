import tkinter as tk
from tkinter import ttk
from random import choice

window = tk.Tk()
window.title("Treeview widget")
window.geometry("600x500")

#data
first_names = ['Alison','Trent','Ibu','Vergil','Andy','Alixes','Ryan','Dominic','Luis','Dieogo','Mo']
last_names = ['Becker','Arnold','Konate','Van Dijk', 'Robertson', 'McAlister', 'Gravenberch', 'Sobo', 'Diaz', 'Jota', 'Salah']

# Treeview
table = ttk.Treeview(window, columns= ('first', 'last', 'email'), show="headings")
table.heading('first', text = "First name")
table.heading('last', text = "Last name")
table.heading('email', text = "Email address")
table.pack(fill= 'both', expand=True)

# Inserting into the table
for i in range(100):
    first = choice(first_names)
    last = choice(last_names)
    email = f'{first}.{last}@gmail.com'
    data = (first, last, email)
    table.insert(parent='', index=0, values = data)

#events
def item_select(event):
    # print(table.selection())
    for i in table.selection():
        print(table.item(i)['values'])

def delete_items(_):
    for i in table.selection():
        table.delete(i)

table.bind('<<TreeviewSelect>>', item_select)
table.bind('<Delete>', delete_items)

window.mainloop()
