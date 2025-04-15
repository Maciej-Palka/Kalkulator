import tkinter

import customtkinter

class App:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title("Kalkulator")
        self.frame = tkinter.Frame(self.root)
        self.frame.pack()


app = App()