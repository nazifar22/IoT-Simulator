import tkinter as tk
from tkinter import ttk

def Style(root):
    # Set a default theme
    style = ttk.Style()

    # Define custom colors
    bg_color = "#ffffff"  
    text_color = "#000000"  
    button_color = "#FFB6C1"  
    slider_color = "#A9A9A9" 

    # Set default font
    default_font = ("Arial", 10)
    root.option_add("*Font", default_font)

    # Configure styles for buttons, labels, and scales
    style.configure("TButton", font=default_font, padding=2, background=button_color, foreground=text_color)
    style.configure("TLabel", font=default_font, background=bg_color, foreground=text_color)
    style.configure("Horizontal.TScale", troughcolor=slider_color, sliderlength=30, sliderrelief="flat")

    # Configure the background color for all widgets
    style.configure("TFrame", background=bg_color)
    style.configure("TLabel", background=bg_color)
    style.configure("TButton", background=button_color)

    # Change button color when it's active
    style.map("TButton",
              background=[('active', button_color)],
              foreground=[('active', text_color)])


