import tkinter as tk
from tkinter import ttk


def get_pos(event):
    print(f'x: {event.x} y: {event.y}')

window = tk.Tk()
window.geometry("600x500")
window.title("Event Binding")

# widgets
text = tk.Text(window)
text.pack()

entry = ttk.Entry(window)
entry.pack()

btn = ttk.Button(window, text= "A Button")
btn.pack()


#events
entry.bind('<KeyPress-a>', lambda event:print("an event was detected"))

entry.bind('<Motion>', get_pos)




window.mainloop()