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
        for i in range(5):  # zakładamy 5 kolumn (0–4)
            self.root.columnconfigure(i, weight=1)

        for i in range(6): self.root.rowconfigure(i, weight=1)


        ctk.set_appearance_mode("white")
        ctk.set_default_color_theme("dark-blue")
        custom_font = ("Times",30,'bold')

        self.lbox = tk.Listbox(self.root)
        self.lbox.grid(row=0, column=1, columnspan=3, rowspan=2, padx=5, pady=5, sticky="nsew")

        self.dot_button = ctk.CTkButton(self.root, text=".", font=custom_font, command=self.placeholder,
                                                height=60, width=60)
        self.dot_button.grid(row=5, column=3, padx=5, pady=5, sticky="nsew")

        self.number_zero_button = ctk.CTkButton(self.root, text="0", font=custom_font, command=self.placeholder,
                                                height=60, width=60)
        self.number_zero_button.grid(row=5, column=2, padx=5, pady=5, sticky="w")

        self.plus_minus_button = ctk.CTkButton(self.root, text="-/+", font=custom_font, command=self.placeholder,
                                                height=60, width=60)
        self.plus_minus_button.grid(row=5, column=1, padx=5, pady=5, sticky="w")

        self.number_one_button = ctk.CTkButton(self.root, text="1", font=custom_font, command=self.placeholder,
                                               height=60, width=60)
        self.number_one_button.grid(row=4, column=1, padx=5, pady=5, sticky="w")

        self.number_two_button = ctk.CTkButton(self.root, text="2", font=custom_font, command=self.placeholder,
                                               height=60, width=60)
        self.number_two_button.grid(row=4, column=2, padx=5, pady=5, sticky="w")

        self.number_three_button = ctk.CTkButton(self.root, text="3", font=custom_font, command=self.placeholder,
                                                 height=60, width=60)
        self.number_three_button.grid(row=4, column=3, padx=5, pady=5, sticky="w")

        self.number_four_button = ctk.CTkButton(self.root, text="4", font=custom_font, command=self.placeholder,
                                                height=60, width=60)
        self.number_four_button.grid(row=3, column=1, padx=5, pady=5, sticky="w")

        self.number_five_button = ctk.CTkButton(self.root, text="5", font=custom_font, command=self.placeholder,
                                                height=60, width=60)
        self.number_five_button.grid(row=3, column=2, padx=5, pady=5, sticky="w")

        self.number_six_button = ctk.CTkButton(self.root, text="6", font=custom_font, command=self.placeholder,
                                               height=60, width=60)
        self.number_six_button.grid(row=3, column=3, padx=5, pady=5, sticky="w")

        self.number_seven_button = ctk.CTkButton(self.root, text="7", font=custom_font, command=self.placeholder,
                                                 height=60, width=60)
        self.number_seven_button.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        self.number_eight_button = ctk.CTkButton(self.root, text="8", font=custom_font, command=self.placeholder,
                                                 height=60, width=60)
        self.number_eight_button.grid(row=2, column=2, padx=5, pady=5, sticky="w")

        self.number_nine_button = ctk.CTkButton(self.root, text="9", font=custom_font, command=self.placeholder,
                                                height=60, width=60)
        self.number_nine_button.grid(row=2, column=3, padx=5, pady=5, sticky="w")



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
