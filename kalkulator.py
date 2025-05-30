from tkinter import simpledialog

import customtkinter as ctk
import math
import cmath
from collections import deque
from datetime import datetime

# funkcja tworząca przyciski
def create_btn(parent, width, height, text, font, row, column, command):
    button = ctk.CTkButton(parent, text=text, font=font, command=command, height=height, width=width)
    button.grid(row=row, column=column, padx=5, pady=5, sticky="nsew")
    return button

class HistoriaOperacji:
    def __init__(self, max_pamiec = 10):
        self.historia =deque(maxlen=max_pamiec)
        self.indeks = -1
        self.tryb_przegladania = False


    def zapisz(self, dzialanie: str, wynik: float):
        wpis = f"{dzialanie} = {wynik}"
        self.historia.append(wpis)
        self.indeks = len(self.historia)-1

    def przelacz_przegladanie(self):
        self.tryb_przegladania = not self.tryb_przegladania
        if self.tryb_przegladania:
            self.index = len(self.historia) - 1

    def czy_tryb_przegladania(self):
        return self.tryb_przegladania

    def pokaz(self):
        if self.tryb_przegladania and 0 <= self.index < len(self.historia):
            return self.historia[self.index]
        return ""

    def nastepne(self):
        if self.tryb_przegladania and self.index < len(self.historia) - 1:
            self.index += 1
        return self.pokaz()

    def poprzednie(self):
        if self.tryb_przegladania and self.index > 0:
            self.index -= 1
        return self.pokaz()

    def pobierz_aktualne_dzialanie(self):
        if self.tryb_przegladania and 0 <= self.index < len(self.historia):
            return self.historia[self.index].split('=')[0].strip()
        return ""
    
    def wyczysc(self):
        self.historia.clear()
        self.indeks = -1
        self.tryb_przegladania = False

    #impor export
    def save_results_to_file(self, filename="./results.txt"):
        try:
            with open(filename, "w") as file:
                for item in self.historia:
                    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    file.write(f"{timestamp} {item}\n")
        except IOError as e:
            print(f"Błąd zapisu do pliku: {e}")
    
    def load_results_from_file(self, filename="results.txt"):
        try:
            with open(filename, "r") as file:
                self.wyczysc()
                for line in file:
                    line = line.strip()
                    if " = " not in line:
                        continue

                    try:
                        date, time, rest = line.split(" ", 2)
                        expression, result = rest.split(" = ")
                        self.zapisz(expression.strip(),result.strip())
                    except ValueError:
                        print(f"Błąd parsowania linii: {line}")
                        continue

        except FileNotFoundError:
            print(f"Plik '{filename}' nie istnieje.")
        except Exception as e:
            print(f"Błąd podczas importu: {e}")

        self.labelSolution.configure(text="Not a complex number", font=self.fontSmall)
        return


class App:
    def __init__(self, disp):

        # zmienne potrzebne później
        self.root = disp
        self.equation = ''
        self.solutionPreview = ''

        # historia
        self.historia = HistoriaOperacji(max_pamiec=10)

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
            ("Hist", 8, 0),("<", 8, 1), (">", 8, 2), ("X", 8, 3), #historia
            ("Import",9,0),("Export",9,1),#import export
            ("(", 3, 0), (")", 3, 1), ("j", 3, 2),  # nowe
            ("7", 4, 0), ("8", 4, 1), ("9", 4, 2), ("/", 2, 3),
            ("4", 5, 0), ("5", 5, 1), ("6", 5, 2), ("*", 3, 3),
            ("1", 6, 0), ("2", 6, 1), ("3", 6, 2), ("-", 4, 3),
            ("0", 7, 0), (".", 7, 1), ("=", 7, 2), ("+", 5, 3),
            ("C", 2, 0), ("B", 2, 1), ("R", 2, 2), ("^", 6, 3),
            ("T", 9, 2), ("E", 9, 3)
        ]

        #stworzenie odpo
        for (text, r, c) in buttons:
            create_btn(self.root, btn_w, btn_h, text, custom_font, r, c, lambda t=text: self.calculate(t))
        self.de_moivre_button = create_btn(self.root, btn_w, btn_h, "De Moivre", custom_font, 7, 3, self.do_de_moivre)
        self.de_moivre_button.grid_remove()

    def do_de_moivre(self):
        val = self.eval_equation(self.equation)
        if not isinstance(val, complex):
            self.labelSolution.configure(text="Not a complex number", font=self.fontSmall)
            return
        n = simpledialog.askinteger("De Moivre", "Podaj wykładnik całkowity n:", parent=self.root, minvalue=1)
        if n is None:
            # User canceled the dialog
            self.de_moivre_button.grid_remove()
            return
        r = abs(val)
        theta = cmath.phase(val)
        r_n = r ** n
        theta_n = theta * n
        result_c = r_n * cmath.rect(1, theta_n)
        self.equation = str(result_c)
        self.labelEquation.configure(text=self.equation, font=self.fontBig)
        theta_deg_n = math.degrees(theta_n)
        trig_result_str = f"{r_n:.5f} (cos {theta_deg_n:.2f}° + i sin {theta_deg_n:.2f}°)"
        self.labelSolution.configure(
            text=f"De Moivre:\n{trig_result_str}",
            font=self.fontSmall
        )
        self.historia.zapisz(f"({val})^{n}", result_c)
        # Hide De Moivre button after use
        self.de_moivre_button.grid_remove()  # Hide De Moivre button
        self.labelSolution.configure(text='', font=self.fontSmall)
    # funkcja licząca
    def eval_equation(self, expr):
        # Dozwolone funkcje i zmienne
        allowed_names = {
            "sqrt": cmath.sqrt
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
            self.historia.zapisz(self.equation, self.solution)
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
        
        elif operator == "Hist":
            if not self.historia.historia:
                self.labelEquation.configure(text="No history", font=self.fontBig)
                self.labelSolution.configure(text='', font=self.fontSmall)
            else:
                self.historia.przelacz_przegladanie()
                self.equation = self.historia.pobierz_aktualne_dzialanie()
                self.labelEquation.configure(text=self.equation, font=self.fontBig)
                self.labelSolution.configure(text=self.eval_equation(self.equation), font=self.fontSmall)

        elif operator == "<":
            if self.historia.czy_tryb_przegladania():
                self.equation = self.historia.poprzednie().split('=')[0].strip()
                self.labelEquation.configure(text=self.equation, font=self.fontBig)
                self.labelSolution.configure(text=self.eval_equation(self.equation), font=self.fontSmall)

        elif operator == ">":
            if self.historia.czy_tryb_przegladania():
                self.equation = self.historia.nastepne().split('=')[0].strip()
                self.labelEquation.configure(text=self.equation, font=self.fontBig)
                self.labelSolution.configure(text=self.eval_equation(self.equation), font=self.fontSmall)
        elif operator == "X":
            if self.historia.czy_tryb_przegladania():
                self.historia.wyczysc()
                self.equation = ''
                self.labelEquation.configure(text='History deleted', font=self.fontBig)
                self.labelSolution.configure(text='', font=self.fontSmall)
        
        elif operator == "Export":
            if not self.historia.historia:
                self.labelEquation.configure(text='No history to export', font=self.fontBig)
            else:
                try:
                    self.historia.save_results_to_file()
                    self.labelEquation.configure(text='History exported', font=self.fontBig)
                except Exception as e:
                    self.labelEquation.configure(text=f'Export failed: {str(e)}', font=self.fontBig)
            self.labelSolution.configure(text='', font=self.fontSmall)

        elif operator == "Import":
            try: 
                self.historia.load_results_from_file()
                self.labelEquation.configure(text='History imported', font=self.fontBig)
            except FileNotFoundError:
                self.labelEquation.configure(text="Import failed!", font=self.fontBig)
                self.labelSolution.configure(text="", font=self.fontSmall)
        elif operator == 'T':
            if self.equation.strip() == '':
                self.labelSolution.configure(text="Enter expression first", font=self.fontSmall)
                return
            val = self.eval_equation(self.equation)
            if isinstance(val, complex):
                r = abs(val)
                theta = cmath.phase(val)
                theta_deg = math.degrees(theta)
                trig_str = f"{r:.5f} (cos {theta_deg:.2f}° + i sin {theta_deg:.2f}°)"
                self.labelSolution.configure(text=trig_str, font=self.fontSmall)
                # Show De Moivre button, hide Trig Form button
                self.de_moivre_button.grid()  # Show De Moivre button
        elif operator == 'E':  # <-- added handler for exponential form
            if self.equation.strip() == '':
                self.labelSolution.configure(text="Enter expression first", font=self.fontSmall)
                return
            val = self.eval_equation(self.equation)
            if isinstance(val, complex):
                r = abs(val)
                theta = cmath.phase(val)
                theta_deg = math.degrees(theta)
                exp_str = f"{r:.5f} e^(i{theta_deg:.2f}°)"
                self.labelSolution.configure(text=exp_str, font=self.fontSmall)
            else:
                self.labelSolution.configure(text="Not a complex number", font=self.fontSmall)
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