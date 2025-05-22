import customtkinter as ctk
import math
import cmath






# funkcja tworząca przyciski
def create_btn(parent, width, height, text, font, row, column, command):
    button = ctk.CTkButton(parent, text=text, font=font, command=command, height=height, width=width)
    button.grid(row=row, column=column, padx=5, pady=5, sticky="nsew")
    return button

class App:
    def __init__(self, disp):

        # zmienne potrzebne później
        self.root = disp
        self.equation = ''
        self.solutionPreview = ''

        # rozmiar czcionki
        self.fontSmall = ctk.CTkFont(size=15)
        self.fontBig = ctk.CTkFont(size=30)

        # parametry okienka/aplikacji
        disp.title("Calculator")
        disp.resizable(False, False)
        ctk.set_default_color_theme("dark-blue")


        # przypisanie wagi do poszczególnych rzędów
        for i in range(4):
            self.root.columnconfigure(i, weight=1)
        for i in range(8):
            self.root.rowconfigure(i, weight=1)


        # ramka z rozwiązaniami
        self.equationsFrame = ctk.CTkFrame(self.root)
        self.equationsFrame.grid(row=0, rowspan=2, column=0, columnspan=5, padx=10, pady=10, sticky="nsew")

        # informacje o aktualnej operacji
        self.labelEquation = ctk.CTkLabel(self.equationsFrame, text='', font=self.fontBig)
        self.labelEquation.grid(row=0, column=0, columnspan=4, padx=10, pady=5, sticky='w')

        self.labelSolution = ctk.CTkLabel(self.equationsFrame, text='', font=self.fontSmall)
        self.labelSolution.grid(row=1, column=0, columnspan=4, padx=10, pady=5, sticky='w')

        # czcionka
        custom_font = ("Times", 20, 'bold')
        btn_w, btn_h = 20, 20

        # --- Rozkład przycisków ---
        buttons = [
            ("(", 3, 0), (")", 3, 1), ("j", 3, 2),  # nowe
            ("7", 4, 0), ("8", 4, 1), ("9", 4, 2), ("/", 2, 3),
            ("4", 5, 0), ("5", 5, 1), ("6", 5, 2), ("*", 3, 3),
            ("1", 6, 0), ("2", 6, 1), ("3", 6, 2), ("-", 4, 3),
            ("0", 7, 0), (".", 7, 1), ("=", 7, 2), ("+", 5, 3),
            ("C", 2, 0), ("B", 2, 1), ("R", 2, 2), ("^", 6, 3)
        ]

        #stworzenie odpo
        for (text, r, c) in buttons:
            create_btn(self.root, btn_w, btn_h, text, custom_font, r, c, lambda t=text: self.calculate(t))

    # funkcja licząca
    def eval_equation(self, expr):
        # Dozwolone funkcje i zmienne
        allowed_names = {
            "sqrt": cmath.sqrt,
            "exp": cmath.exp,
            "j": 1j,
            "complex": complex,
            "re": lambda x: x.real,
            "im": lambda x: x.imag,
        }

        try:
            # zamień potęgowanie ^ na **
            expr = expr.replace('^', '**')

            # ewaluacja wyrażenia z ograniczonym zakresem
            result = eval(expr, {"__builtins__": None}, allowed_names)

            # zaokrąglenie wyników rzeczywistych
            if isinstance(result, complex):
                result = complex(round(result.real, 5), round(result.imag, 5))
            elif isinstance(result, (int, float)):
                result = round(result, 5)

            return result
        except Exception:
            return "Error"

    # funkcja od wykonywania operatorów
    def calculate(self, operator):
        if operator == 'C':
            self.equation = ''
            self.solution = ''
            self.labelEquation.configure(text='')
            self.labelSolution.configure(text='')

        elif operator == '=':
            self.solution = ''
            self.solution = self.eval_equation(self.equation)
            self.labelEquation.configure(text=self.solution, font=self.fontBig)
            self.labelSolution.configure(text='')
            self.solution = ''

        elif operator == 'B':
            self.equation = self.equation[:-1]
            self.solutionPreview = self.eval_equation(self.equation)
            self.labelEquation.configure(text=self.equation, font=self.fontBig)
            self.labelSolution.configure(text=self.solutionPreview, font=self.fontSmall)

        elif operator == 'R':
            try:
                value = self.eval_equation(self.equation)
                if isinstance(value, str) and value == "Error":
                    raise ValueError()
                self.solution = cmath.sqrt(value)
                if isinstance(self.solution, complex):
                    self.solution = complex(round(self.solution.real, 5), round(self.solution.imag, 5))
                else:
                    self.solution = round(self.solution, 5)
            except:
                self.solution = 'Error'
            self.labelEquation.configure(text=self.solution, font=self.fontBig)
            self.labelSolution.configure(text='')

        else:
            self.equation += str(operator)
            self.solutionPreview = self.eval_equation(self.equation)
            self.labelEquation.configure(text=self.equation, font=self.fontBig)
            self.labelSolution.configure(text=self.solutionPreview, font=self.fontSmall)


if __name__ == "__main__":
    ctk.set_default_color_theme("dark-blue")
    root = ctk.CTk()
    root.geometry("400x500")
    app = App(root)
    root.mainloop()
