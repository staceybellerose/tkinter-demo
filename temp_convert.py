from tkinter import *
from tkinter import ttk

def fahrenheit_to_celsius():
    """Convert the value for Fahrenheit to Celsius and insert the
    result into lbl_result.
    """
    fahrenheit = ent_temperature.get()
    celsius = (5/9) * (float(fahrenheit) - 32)
    lbl_result["text"] = f"{round(celsius, 2)} \N{DEGREE CELSIUS}"

# Set-up the window
window = Tk()
window.title("Temperature Converter")
window.resizable(width=False, height=False)

# Create the Fahrenheit entry frame with an Entry
# widget and label in it
frm = ttk.Frame(master=window)
ent_temperature = ttk.Entry(master=frm, width=10)
lbl_temp = ttk.Label(master=frm, text="\N{DEGREE FAHRENHEIT}")

# Create the conversion Button and result display Label
btn_convert = ttk.Button(
    master=frm,
    text="\N{RIGHTWARDS BLACK ARROW}",
    command=fahrenheit_to_celsius,
    width=2
)
lbl_result = ttk.Label(master=frm, text="\N{DEGREE CELSIUS}")

# Layout the temperature Entry and Label in frm
# using the .grid() geometry manager
ent_temperature.grid(row=0, column=0, sticky="e")
lbl_temp.grid(row=0, column=1, sticky="w")
btn_convert.grid(row=0, column=2, pady=10, padx=10)
lbl_result.grid(row=0, column=3, padx=10)

# Set-up the layout using the .grid() geometry manager
frm.grid(row=0, column=0, sticky="nesw")

# Run the application
window.mainloop()

