import customtkinter as ctk
import math

def create_btn(parent, width, height, text, font, row, column, command):
    button = ctk.CTkButton(parent, text=text, font=font, command=command, height=height, width=width)
    button.grid(row=row, column=column, padx=5, pady=5, sticky="nsew")
    return button

class App:
    def __init__(self, disp):

        self.root = disp
        self.equation = ''
        self.solutionPreview = ''

        self.fontSmall = ctk.CTkFont(size=15)
        self.fontBig = ctk.CTkFont(size=30)

        disp.title("Calculator")
        disp.resizable(False, False)

        for i in range(4):
            self.root.columnconfigure(i, weight=1)
        for i in range(7):
            self.root.rowconfigure(i, weight=1)

        #ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("dark-blue")

        self.equationsFrame = ctk.CTkFrame(self.root)
        self.equationsFrame.grid(row=0, rowspan=2, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

        self.labelEquation = ctk.CTkLabel(self.equationsFrame, text='', font=self.fontBig)
        self.labelEquation.grid(row=0, column=0, columnspan=4, padx=10, pady=5, sticky='w')

        self.labelSolution = ctk.CTkLabel(self.equationsFrame, text='', font=self.fontSmall)
        self.labelSolution.grid(row=1, column=0, columnspan=4, padx=10, pady=5, sticky='w')

        custom_font = ("Times", 15, 'bold')
        btn_w, btn_h = 20, 20

        # --- Buttons layout ---
        buttons = [
            ("7", 3, 0), ("8", 3, 1), ("9", 3, 2), ("/", 2, 3),
            ("4", 4, 0), ("5", 4, 1), ("6", 4, 2), ("*", 3, 3),
            ("1", 5, 0), ("2", 5, 1), ("3", 5, 2), ("-", 4, 3),
            ("0", 6, 0), (".", 6, 1), ("=", 6, 2), ("+", 5, 3),
            ("C", 2, 0), ("B", 2, 1), ("R", 2, 2),
        ]

        for (text, r, c) in buttons:
            create_btn(self.root, btn_w, btn_h, text, custom_font, r, c, lambda t=text: self.calculate(t))

    def calculate(self, operator):
        if operator == 'C':
            self.equation = ''
            self.solutionPreview = ''
            self.labelEquation.configure(text='')
            self.labelSolution.configure(text='')

        elif operator == '=':
            try:
                result = round(eval(self.equation), 5)
                self.labelEquation.configure(text=str(result))
                self.labelSolution.configure(text='')
                self.equation = str(result)
            except:
                self.labelEquation.configure(text="Error")
                self.equation = ''

        elif operator == 'B':
            self.equation = self.equation[:-1]
            try:
                self.solutionPreview = str(round(eval(self.equation), 5))
            except:
                self.solutionPreview = ''
            self.labelEquation.configure(text=self.equation)
            self.labelSolution.configure(text=self.solutionPreview)

        elif operator == 'R':
            try:
                result = math.sqrt(eval(self.equation))
                result = round(result, 5)
                self.labelEquation.configure(text=str(result))
                self.labelSolution.configure(text='')
                self.equation = str(result)
            except:
                self.labelEquation.configure(text="Error")
                self.equation = ''

        else:
            self.equation += str(operator)
            try:
                self.solutionPreview = str(round(eval(self.equation), 5))
            except:
                self.solutionPreview = ''
            self.labelEquation.configure(text=self.equation)
            self.labelSolution.configure(text=self.solutionPreview)

if __name__ == "__main__":
    ctk.set_default_color_theme("dark-blue")
    root = ctk.CTk()
    root.geometry("400x500")
    app = App(root)
    root.mainloop()
