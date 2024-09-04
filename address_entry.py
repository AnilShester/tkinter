import tkinter as tk

window = tk.Tk()
window.title("Adress Entry Form")
window.geometry("600x400")


#define grid layout
# window.rowconfigure((0,1,2,3,4,5,6,7), weight=1)
# window.columnconfigure(0, weight=1)
# window.columnconfigure(1, weight=5)

# creating widgets
first_name = tk.Label(window, text="First Name:", background='red')
last_name = tk.Label(window, text="Last Name:")
address_1 = tk.Label(window, text="Address Line 1:")
address_2 = tk.Label(window, text="Address Line 2:")
city = tk.Label(window, text="City:")
state = tk.Label(window, text="State/Province:")
postal_code = tk.Label(window, text="Postal Code:")
country = tk.Label(window, text="Country:")

first_name_entry = tk.Entry(window, background='yellow')
last_name_entry = tk.Entry(window)
address_1_entry = tk.Entry(window)
address_2_entry = tk.Entry(window)
city_entry = tk.Entry(window)
state_entry = tk.Entry(window)
postal_code_entry = tk.Entry(window)
country_entry = tk.Entry(window)

first_name.grid(row=0, column=0, sticky='es')
first_name_entry.grid(row=0, column=1, sticky='ews', padx=5)

last_name.grid(row=1, column=0, sticky='es')
last_name_entry.grid(row=1, column=1, sticky='ews', padx=5)

address_1.grid(row=2, column=0, sticky='es')
address_1_entry.grid(row=2, column=1, sticky='ews', padx=5)

address_2.grid(row=3, column=0, sticky='es')
address_2_entry.grid(row=3, column=1, sticky='ews', padx=5)

city.grid(row=4, column=0, sticky='es')
city_entry.grid(row=4, column=1, sticky='ews', padx=5)

state.grid(row=5, column=0, sticky='es')
state_entry.grid(row=5, column=1, sticky='ews', padx=5)

postal_code.grid(row=6, column=0, sticky='es')
postal_code_entry.grid(row=6, column=1, sticky='ewsn', padx=5)

country.grid(row=7, column=0, sticky='es')
country_entry.grid(row=7, column=1, sticky='ews', padx=5)




window.mainloop()