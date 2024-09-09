import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry('600x500')
window.title("Frames and Parenting")

#frames
frame = ttk.Frame(window, width=100, height=200, borderwidth=10, relief=tk.GROOVE)
frame.pack()

# parenting or master settings 
label = ttk.Label(frame, text='Label inside the frame')
label.pack()

button = ttk.Button(frame, text="A very long Button inside of a frame")
button.pack()

label2 = ttk.Label(window, text="Label outside the frame")
label2.pack()



window.mainloop()