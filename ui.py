import tkinter as tk  # for later
import customtkinter as ctk
from tkinter import *  # for later
from customtkinter import filedialog  # for later
import os  # for later

# Funkcja tworząca przycisk
def create_btn(parent, width, height, text, font, row, column, command):
    button = ctk.CTkButton(parent, text=text, font=font, command=command, height=height, width=width) # , corner_radius=10 # Dodać żeby bardziej zaokrąglić rogi
    button.grid(row=row, column=column, padx=5, pady=5, sticky="nsew")
    return button


class App:
    def __init__(self, root):
        # Inicjalizacja elementów
        self.root = root
        self.create_widgets()

        root.title("Calculator")
        root.resizable(height=False, width=False)

    # Tworzenie widget'ów
    def create_widgets(self):
        for i in range(5):  # zakładamy 5 kolumn (0–4)
            self.root.columnconfigure(i, weight=1)

        for i in range(6): self.root.rowconfigure(i, weight=1)


        ctk.set_appearance_mode("white")
        ctk.set_default_color_theme("dark-blue")
        custom_font = ("Times",30,'bold')

        btn_width = 60
        btn_height = 60

        self.lbox = tk.Listbox(self.root)
        self.lbox.grid(row=0, column=1, columnspan=3, rowspan=2, padx=5, pady=5, sticky="nsew")

        # Tworzenie przycisków
        create_btn(self.root, btn_height, btn_width, ".", custom_font, 5, 3, self.placeholder)
        create_btn(self.root, btn_height, btn_width, "0", custom_font, 5, 2, self.placeholder)
        create_btn(self.root, btn_height, btn_width, "+/-", custom_font, 5, 1, self.placeholder)
        create_btn(self.root, btn_height, btn_width, "1", custom_font, 4, 1, self.placeholder)
        create_btn(self.root, btn_height, btn_width, "2", custom_font, 4, 2, self.placeholder)
        create_btn(self.root, btn_height, btn_width, "3", custom_font, 4, 3, self.placeholder)
        create_btn(self.root, btn_height, btn_width, "4", custom_font, 3, 1, self.placeholder)
        create_btn(self.root, btn_height, btn_width, "5", custom_font, 3, 2, self.placeholder)
        create_btn(self.root, btn_height, btn_width, "6", custom_font, 3, 3, self.placeholder)
        create_btn(self.root, btn_height, btn_width, "7", custom_font, 2, 1, self.placeholder)
        create_btn(self.root, btn_height, btn_width, "8", custom_font, 2, 2, self.placeholder)
        create_btn(self.root, btn_height, btn_width, "9", custom_font, 2, 3, self.placeholder)



    # Funkcja tworząca etykietę
    def create_label(self, parent, row, column, label_text):
        label = ctk.CTkLabel(parent, text=f"{label_text} ", font=("Arial", 12))
        label.grid(row=row, column=column, sticky="nw", columnspan=1, pady=2)
        return label

    # Funkcja testowa
    def placeholder(self):
        print("placeholder")


if __name__ == "__main__":
    root = ctk.CTk()
    root.geometry("320x500")
    app = App(root)
    root.mainloop()
