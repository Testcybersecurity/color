# Simple graphical program to find a color code
# Shows RGB and HEX values of the selected color

import tkinter as tk
from tkinter import colorchooser


def choose_color():
    color = colorchooser.askcolor(title="Choose a color")
    if color[0] is not None:
        r, g, b = map(int, color[0])
        hex_color = color[1]

        result_label.config(
            text=f"RGB: ({r}, {g}, {b})\nHEX: {hex_color}"
        )
        color_preview.config(bg=hex_color)


# Create main window
root = tk.Tk()
root.title("Color Code Finder")
root.geometry("300x200")

# Button to choose color
btn = tk.Button(root, text="Choose Color", command=choose_color)
btn.pack(pady=10)

# Label to show result
result_label = tk.Label(root, text="RGB: \nHEX: ", font=("Arial", 12))
result_label.pack(pady=10)

# Color preview box
color_preview = tk.Label(root, text="     ", width=20, height=2, bg="white")
color_preview.pack(pady=10)

# Run the program
root.mainloop()