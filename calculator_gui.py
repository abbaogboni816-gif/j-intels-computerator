"""Calculator GUI"""
import tkinter as tk
from calculator import add, subtract, multiply, divide, find_modulus, find_square_root

# Create window
window = tk.Tk()
window.title("J-Intels Computerator")
window.geometry("1080x1024")
window.configure(bg="black")

# Configuration
font = ("Arial", 23)
background_color = "black"
button_color = "gray"
justify = "center"

# Create display
display = tk.Entry(window, width=30, borderwidth=5)
display.grid(row=0, column=0, columnspan=4, padx=5, pady=20)
display.configure(font=font, bg="white", fg="black", justify=justify)

# Button configuration
button_color = "gray"
button_width = 5
button_height = 2
button_font = ("Arial", 18)
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"],
    ["C", "√", "%"],
    ["Cos", "sin", "tan"]
]

# Define button actions
def on_button_click(button_text):
    """Handle button clicks"""
    if button_text == "C":
        display.delete(0, tk.END)
    elif button_text == "=":
        try:
            result = eval(display.get())
            display.delete(0, tk.END)
            display.insert(tk.END, str(result))
        except:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")
    elif button_text == "√":
        try:
            result = find_square_root(float(display.get()))
            display.delete(0, tk.END)
            display.insert(tk.END, str(result))
        except:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")
    else:
        display.insert(tk.END, button_text)

# Create buttons
for row_index, button_row in enumerate(buttons):
    for col_index, button_text in enumerate(button_row):
        button = tk.Button(
            window, 
            text=button_text, 
            width=button_width, 
            height=button_height, 
            font=button_font, 
            bg=button_color, 
            fg="white",
            command=lambda text=button_text: on_button_click(text)
        )
        button.grid(row=row_index + 1, column=col_index, padx=5, pady=5)

# Start the app
window.mainloop()
