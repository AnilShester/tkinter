from tkinter import *
# creating a root window from as an instance of TK class of tkinter module
root = Tk()

# creating windows features
root.title("Tk Frame Example")                # creating the title of the window
root.configure(background="skyblue")     # backkground color change
root.maxsize(1300,1000)

#creating a frame widget
left_frame = Frame(root, width=200, height=900, background="maroon")
left_frame.grid(row=0, column=0, padx=10, pady=5)


# creating a left original image frame
left_image_frame = Frame(left_frame, width =300, height=300,   background="red")
left_image_frame.grid(row=2, column=0, padx=20, pady=20)

# create a label above toolbox
Label(left_frame, text="Original Image").grid(row=1, column=0, padx=5, pady=10)

# create a toolbox frame
left_toolbox = Frame(left_frame, width=300, height= 500, background="green")
left_toolbox.grid(row=3, column=0, padx=10, pady=10)


# create right Photo edit frame
right_frame = Frame(root, width= 800, height=800, background="blue")
right_frame.grid(row=0, column=1, padx= 30, pady=10)


root.mainloop()                         