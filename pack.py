import tkinter as tk

window = tk.Tk()
window.geometry('600x500')
window.title("Pack Layout")

# widgets
label1 = tk.Label(window, text= "Label 1", background="green")
label2 = tk.Label(window, text= "Second label", background="blue")
label3 = tk.Label(window, text= "Last label", background="red")
button = tk.Button(window, text="Button")


# layouts
label1.pack(side='top', fill='both', ipadx=5, ipady=10)
label2.pack(side='top', expand=True)
label3.pack(side='top', expand=True, fill='both')
button.pack(side='top', fill='both', ipadx=10, ipady=10)


window.mainloop()
