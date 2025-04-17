import tkinter as tk  # for later
import customtkinter as ctk
from tkinter import *  # for later
from customtkinter import filedialog  # for later
import os  # for later


class App:
    def __init__(self, root):
        # Inicjalizacja elementów
        self.root = root
        self.create_widgets()

        root.title("Calculator")
        root.resizable(height=False, width=False)

    # Tworzenie widget'ów
    def create_widgets(self):
        padx_images = 10
        ctk.set_appearance_mode("white")
        ctk.set_default_color_theme("dark-blue")

        self.number_zero_button = ctk.CTkButton(self.root, text="0", command=self.placeholder, height = 60, width = 60)
        self.number_zero_button.grid(row=8, column=3, pady=5, sticky="w")


    # Funkcja tworząca etykietę
    def create_label(self, parent, row, column, label_text):
        label = ctk.CTkLabel(parent, text=f"{label_text} ", font=("Arial", 12))
        label.grid(row=row, column=column, sticky="nw", columnspan=1, pady=2)
        return label

    def placeholder(self):
        print("placeholder")


if __name__ == "__main__":
    root = ctk.CTk()
    root.geometry("320x500")
    app = App(root)
    root.mainloop()
