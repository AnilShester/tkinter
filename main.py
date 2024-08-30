from tkinter import *
# creating a root window from as an instance of TK class of tkinter module
root = Tk()

root.title("Tk Example")
root.configure(background="yellow")
root.minsize(200, 200) #width and height
root.maxsize(500, 500)
root.geometry("300x300+50+50")
root.mainloop()