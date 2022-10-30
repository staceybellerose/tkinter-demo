from tkinter import *
from tkinter import ttk

def fahrenheit_to_celsius():
    """Convert the value for Fahrenheit to Celsius and insert the
    result into lbl_result.
    """
    fahrenheit = ent_fahrenheit.get()
    if fahrenheit != "":
        celsius = (5/9) * (float(fahrenheit) - 32)
        ent_celsius.delete(0, END)
        ent_celsius.insert(0, celsius)

def celsius_to_fahrenheit():
    """Convert the value for Celsius to Fahrenheit and insert the
    result into ent_temperature.
    """
    celsius = ent_celsius.get()
    if celsius != "":
        fahrenheit = float(celsius) * 9 / 5 + 32
        ent_fahrenheit.delete(0, END)
        ent_fahrenheit.insert(0, fahrenheit)

# Set-up the window and frame
window = Tk()
window.title("Temperature Converter")
window.resizable(width=False, height=False)
frm = ttk.Frame(master=window)

# Create the Fahrenheit Entry widget and label
ent_fahrenheit = ttk.Entry(master=frm, width=10, justify="right")
lbl_fahrenheit = ttk.Label(master=frm, text="\N{DEGREE FAHRENHEIT}")

# Create the conversion Buttons
btn_convert_to_c = ttk.Button(
    master=frm,
    text="\N{RIGHTWARDS ARROW}",
    command=fahrenheit_to_celsius,
    width=2
)
btn_convert_to_f = ttk.Button(
    master=frm,
    text="\N{LEFTWARDS ARROW}",
    command=celsius_to_fahrenheit,
    width=2
)

# Create the Celsius Entry widget and label
ent_celsius = ttk.Entry(master=frm, width=10, justify="right")
lbl_celsius = ttk.Label(master=frm, text="\N{DEGREE CELSIUS}")

# Layout the widgets in the frame using the .grid() geometry manager
ent_fahrenheit.grid(row=0, column=0, sticky="e", rowspan=2)
lbl_fahrenheit.grid(row=0, column=1, sticky="w", rowspan=2)
btn_convert_to_c.grid(row=0, column=2, padx=10)
btn_convert_to_f.grid(row=1, column=2, padx=10)
ent_celsius.grid(row=0, column=3, sticky="e", rowspan=2)
lbl_celsius.grid(row=0, column=4, sticky="w", rowspan=2)

# Set-up the layout using the .grid() geometry manager
frm.grid(row=0, column=0, sticky="nesw", padx=10, pady=10)

# Run the application
window.mainloop()

