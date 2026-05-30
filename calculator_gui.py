"""
Calculator GUI Application

A professional Tkinter-based graphical calculator interface.
Supports basic arithmetic, square root, and trigonometric functions.
"""

import math
import tkinter as tk
from calculator import find_square_root


window = tk.Tk()
window.title("J-Intels Calculator")
window.geometry("500x650")
window.configure(bg="#2c3e50")
window.resizable(False, False)

font_display = ("Arial", 28, "bold")
font_buttons = ("Arial", 16, "bold")
background_color = "#2c3e50"
button_color = "#34495e"
button_hover = "#1a252f"
text_color = "white"

display = tk.Entry(window, width=20, borderwidth=3, relief=tk.RAISED)
display.grid(row=0, column=0, columnspan=4, padx=10, pady=20, sticky="nsew")
display.configure(
    font=font_display,
    bg="#ecf0f1",
    fg="#2c3e50",
    justify="right",
    insertbackground="#34495e",
)

button_width = 4
button_height = 2
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"],
    ["C", "sqrt", "%", "Backspace"],
    ["cos", "sin", "tan", "pi"],
]


def on_button_click(button_text):
    """Handle button clicks with proper error handling."""
    current = display.get()

    try:
        if button_text == "C":
            display.delete(0, tk.END)

        elif button_text == "Backspace":
            if current:
                display.delete(len(current) - 1, tk.END)

        elif button_text == "=":
            result = eval(current, {"__builtins__": {}}, {})
            display.delete(0, tk.END)
            display.insert(tk.END, str(round(result, 10)))

        elif button_text == "sqrt":
            if current:
                result = find_square_root(float(current))
                display.delete(0, tk.END)
                display.insert(tk.END, str(round(result, 10)))

        elif button_text == "pi":
            display.insert(tk.END, str(round(math.pi, 10)))

        elif button_text == "sin":
            if current:
                result = math.sin(math.radians(float(current)))
                display.delete(0, tk.END)
                display.insert(tk.END, str(round(result, 10)))

        elif button_text == "cos":
            if current:
                result = math.cos(math.radians(float(current)))
                display.delete(0, tk.END)
                display.insert(tk.END, str(round(result, 10)))

        elif button_text == "tan":
            if current:
                result = math.tan(math.radians(float(current)))
                display.delete(0, tk.END)
                display.insert(tk.END, str(round(result, 10)))

        else:
            display.insert(tk.END, button_text)

    except ValueError:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")
    except ZeroDivisionError:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error: Div by 0")
    except Exception:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")


for row_index, button_row in enumerate(buttons):
    for col_index, button_text in enumerate(button_row):
        def create_command(text):
            return lambda: on_button_click(text)

        if button_text == "=":
            btn_bg = "#27ae60"
            btn_fg = "white"
        elif button_text == "C":
            btn_bg = "#e74c3c"
            btn_fg = "white"
        elif button_text in ["/", "*", "-", "+", "%", "sqrt", "Backspace"]:
            btn_bg = "#3498db"
            btn_fg = "white"
        elif button_text in ["sin", "cos", "tan", "pi"]:
            btn_bg = "#9b59b6"
            btn_fg = "white"
        else:
            btn_bg = button_color
            btn_fg = text_color

        button = tk.Button(
            window,
            text=button_text,
            width=button_width,
            height=button_height,
            font=font_buttons,
            bg=btn_bg,
            fg=btn_fg,
            activebackground=button_hover,
            activeforeground="white",
            relief=tk.RAISED,
            bd=2,
            command=create_command(button_text),
        )
        button.grid(row=row_index + 1, column=col_index, padx=5, pady=5, sticky="nsew")

for i in range(7):
    window.grid_rowconfigure(i, weight=1)
for i in range(4):
    window.grid_columnconfigure(i, weight=1)

if __name__ == "__main__":
    window.mainloop()
