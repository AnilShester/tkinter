import tkinter as tk

window = tk.Tk()
window.geometry('600x900')
window.title("Layout with frame and pack")

# widgets
label1 = tk.Label(window, text="First Label", background='red')
label2 = tk.Label(window, text='Label 2', background='blue')
label3 = tk.Label(window, text="Another Label", background="green")

frame = tk.Frame(window)

button1 = tk.Button(frame, text = "A button")
label4 = tk.Label(frame, text="last of the labels", background='orange')
button2 = tk.Button(frame, text="another button")
button3 = tk.Button(frame, text="Button 3")
button4 = tk.Button(frame, text="Button 4")
button5 = tk.Button(frame, text="Button 5")

# layout

label1.pack(side='top', expand=True, fill='both')
label2.pack(side='top', expand=True, fill='both')
label3.pack(side='top', expand=True)

frame.pack(side= 'top', expand=True ,fill='both', padx=10, pady=20)

button1.pack(side='left', expand=True, fill='both')
label4.pack(side='left', expand= True, fill='both')
button2.pack(side='left', expand=True, fill='both')
button3.pack(side='top', expand=True, fill='both')
button4.pack(side='top', expand= True, fill='both')
button5.pack(side='top', expand=True, fill='both')


window.mainloop()
