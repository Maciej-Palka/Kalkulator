from collections import deque



'''
# ilość przechowywaneych działań w pamieci ,
# działania wpisywane w postaci "2 + 2 = 4"
# zapisywanie polega na wpisaniu komendy w poostaci jak w 21 linijce działania i wynik w osobnej
history = deque(maxlen=10)

def zapisz_operacje(dzialanie: str, wynik: float):

    wpis = f"{dzialanie} = {wynik}"
    history.append(wpis)

def pokaz_historie():
    if not history:
        print("Brak zapisanych dzialan")
        return
    for i, wpis in enumerate(history,1):
        print(f"{i}: {wpis}")
    return
'''

class HistoriaOperacji:
    def __init__(self, max_pamiec = 10):
        self.historia =deque(maxlen=max_pamiec)
        self.indeks = -1
        self.tryb_przegladania = False

    def zapisz(self, dzialanie: str, wynik: float):
        wpis = f"{dzialanie} = {wynik}"
        self.historia.append(wpis)
        self.indeks = len(self.historia)-1

    def pokaz(self):
        if not self.historia:
            return
        if 0 <= self.indeks < len(self.historia):
            return self.historia[self.indeks]


    def wyczysc(self):
        self.historia.clear()
        self.indeks = -1
        self.tryb_przegladania = False


    def nastepne(self):
        if self.indeks < len(self.historia) - 1:
            self.indeks += 1
        return self.pokaz()

    def poprzednie(self):
        if self.indeks > 0:
            self.indeks -= 1
        return self.pokaz()

    def przelacz_przegladanie(self):
        self.tryb_przegladania = not self.tryb_przegladania
        if self.tryb_przegladania:
            self.indeks = len(self.historia) - 1
        else:
            self.indeks = -1

historia = HistoriaOperacji()

historia.zapisz("2 + 2",4)
historia.zapisz("3 + 5",8)
historia.zapisz("5 + 5",10)
historia.zapisz("2 - 1",1)

historia.przelacz_przegladanie()
print(historia.pokaz())     # pokazuje ostatni wpis
print(historia.poprzednie())
print(historia.poprzednie())
print(historia.nastepne())

# Czyszczenie:
historia.wyczysc()
print(historia.pokaz())



'''
zapisz_operacje("2 + 2", 4)
zapisz_operacje("3 + 2", 3)
zapisz_operacje("2 - 1", 2)
pokaz_historie()
'''