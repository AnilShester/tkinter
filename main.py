from tkinter import *
# creating a root window from as an instance of TK class of tkinter module
root = Tk()

# creating windows features
root.title("Tk Frame Example")                # creating the title of the window
root.configure(background="skyblue")          # backkground color change
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


# declaring string variables for storing username and password
username_var = StringVar()
password_var = StringVar()
texts = StringVar()

# labels for username and password
username_label = Label( left_toolbox, text="Username")
password_label = Label(left_toolbox, text="Password")



# create a text entry box
username_entry = Entry(left_toolbox, textvariable=username_var, width=30, bd=2)
password_entry = Entry(left_toolbox, textvariable=password_var, width=30, bd=2)


# retreving the entry


#function for clicking buttons
def button_click():
    username = username_var.get()
    password = password_var.get()
    print(f"your username is {username} and password is {password}")


# create a button
login_btn = Button(left_toolbox, text="LOGIN", width=30, command=button_click)
logoff_btn = Button(left_toolbox, text="LOGOFF", width=30, command=root.quit)

username_label.grid(row=0, column=0, padx=5, pady=5)
username_entry.grid(row=0, column=1)
password_label.grid(row=1, column=0)
password_entry.grid(row=1, column=1)
login_btn.grid(row=2, column=0)
logoff_btn.grid(row=2,column=1)


root.mainloop()