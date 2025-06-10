import tkinter as tk
from tkinter import ttk

# Conversion logic
def convert():
    value = float(entry.get())
    from_unit = from_unit_var.get()
    to_unit = to_unit_var.get()
    
    # Conversion to meters (base)
    if from_unit == "Kilometer":
        value_in_meters = value * 1000
    elif from_unit == "Mile":
        value_in_meters = value * 1609.34
    elif from_unit == "Centimeter":
        value_in_meters = value / 100
    else:  # Meter
        value_in_meters = value

    # Convert from meters to target unit
    if to_unit == "Kilometer":
        result = value_in_meters / 1000
    elif to_unit == "Mile":
        result = value_in_meters / 1609.34
    elif to_unit == "Centimeter":
        result = value_in_meters * 100
    else:  # Meter
        result = value_in_meters

    result_label.config(text=f"{result:.4f} {to_unit}")

# GUI Setup
root = tk.Tk()
root.title("Unit Converter")
root.geometry("350x200")
root.configure(bg="white")

tk.Label(root, text="Enter Value:", bg="white").pack()
entry = tk.Entry(root)
entry.pack()

from_unit_var = tk.StringVar(value="Meter")
to_unit_var = tk.StringVar(value="Kilometer")

tk.Label(root, text="From Unit:", bg="white").pack()
from_menu = ttk.Combobox(root, textvariable=from_unit_var, values=["Meter", "Kilometer", "Centimeter", "Mile"])
from_menu.pack()

tk.Label(root, text="To Unit:", bg="white").pack()
to_menu = ttk.Combobox(root, textvariable=to_unit_var, values=["Meter", "Kilometer", "Centimeter", "Mile"])
to_menu.pack()

tk.Button(root, text="Convert", command=convert).pack(pady=5)
result_label = tk.Label(root, text="", font=("Arial", 14), bg="white", fg="blue")
result_label.pack()

root.mainloop()
