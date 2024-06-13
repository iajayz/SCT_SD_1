import tkinter as tk
from tkinter import ttk

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)

def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)

def convert_temperature():
    try:
        temp = float(entry_temp.get())
        conversion_type = conversion_var.get()

        if conversion_type == "Celsius to Fahrenheit":
            result = celsius_to_fahrenheit(temp)
            result_label.config(text=f"{temp}°C is {result:.2f}°F")
        elif conversion_type == "Fahrenheit to Celsius":
            result = fahrenheit_to_celsius(temp)
            result_label.config(text=f"{temp}°F is {result:.2f}°C")
        elif conversion_type == "Celsius to Kelvin":
            result = celsius_to_kelvin(temp)
            result_label.config(text=f"{temp}°C is {result:.2f}K")
        elif conversion_type == "Kelvin to Celsius":
            result = kelvin_to_celsius(temp)
            result_label.config(text=f"{temp}K is {result:.2f}°C")
        elif conversion_type == "Fahrenheit to Kelvin":
            result = fahrenheit_to_kelvin(temp)
            result_label.config(text=f"{temp}°F is {result:.2f}K")
        elif conversion_type == "Kelvin to Fahrenheit":
            result = kelvin_to_fahrenheit(temp)
            result_label.config(text=f"{temp}K is {result:.2f}°F")
        else:
            result_label.config(text="Invalid conversion type selected.")
    except ValueError:
        result_label.config(text="Please enter a valid number.")

# Create main application window
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("800x600")
root.configure(bg="#e0f7fa")

# Create and place the widgets
frame = ttk.Frame(root, padding="20 20 20 20", style="My.TFrame")
frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

style = ttk.Style()
style.configure("TLabel", font=("Helvetica", 20))
style.configure("TEntry", font=("Helvetica", 20))
style.configure("TCombobox", font=("Helvetica", 20))
style.configure("My.TFrame", background="#e0f7fa")

ttk.Label(frame, text="Temperature:", style="TLabel").grid(column=1, row=1, sticky=tk.W)
entry_temp = ttk.Entry(frame, width=20, style="TEntry")
entry_temp.grid(column=2, row=1, sticky=(tk.W, tk.E))

ttk.Label(frame, text="Conversion:", style="TLabel").grid(column=1, row=2, sticky=tk.W)
conversion_var = tk.StringVar()
conversion_combobox = ttk.Combobox(frame, textvariable=conversion_var, style="TCombobox")
conversion_combobox['values'] = (
    "Celsius to Fahrenheit",
    "Fahrenheit to Celsius",
    "Celsius to Kelvin",
    "Kelvin to Celsius",
    "Fahrenheit to Kelvin",
    "Kelvin to Fahrenheit"
)
conversion_combobox.grid(column=2, row=2, sticky=(tk.W, tk.E))
conversion_combobox.current(0)

# Use tkinter Button widget for more control
convert_button = tk.Button(frame, text="Convert", command=convert_temperature, font=("Helvetica", 20, "bold"),
                           bg="#00695c", fg="white", activebackground="#004d40", activeforeground="white")
convert_button.grid(column=2, row=3, sticky=tk.W)

result_label = ttk.Label(frame, text="", style="TLabel")
result_label.grid(column=1, row=4, columnspan=2, sticky=(tk.W, tk.E))

# Add padding to all widgets
for child in frame.winfo_children():
    child.grid_configure(padx=10, pady=10)

# Start the Tkinter event loop
root.mainloop()
