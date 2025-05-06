import cmath
import math

def input_complex():
    while True:
        s = input("Wpisz liczbę zespoloną np. 2+3i lub wpisz '=' żeby wpisać części osobno").strip()
        if s.lower() == '=':
            try:
                Re = float(input("Podaj część rzeczywistą: ").strip())
                Im = float(input("Podaj część urojoną: ").strip())
                return complex(Re, Im)
            except ValueError:
                print("Błędne dane")
        else:
            try:
                s_mod = s.replace('i', 'j')
                z = complex(s_mod)
                return z
            except ValueError:
                print("Błędne dane, podaj liczbę jeszcze raz")


