import tkinter as tk

window = tk.Tk()
window.title("GRID")
window.geometry("600x400")

#widgets
label1 = tk.Label(window, text="Label 1", background="red")
label2 = tk.Label(window, text="Label 2", background="blue")
label3 = tk.Label(window, text="Label 3", background="green")
label4 = tk.Label(window, text="Label 4", background="yellow")
button1 = tk.Button(window, text='Button 1')
button2 = tk.Button(window, text="Button 2")
entry = tk.Entry(window)

# define a grid
window.columnconfigure((0,1,2), weight = 1)
window.columnconfigure(3, weight = 5)
window.rowconfigure(0, weight = 1)

# place widget
label1.grid(row=0, column=0, sticky="ewns")
label2.grid(row=0, column=1, sticky='ewsn')
label3.grid(row=0, column=3, sticky='ew')

window.mainloop()



