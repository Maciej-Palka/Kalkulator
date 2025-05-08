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

    def zapisz(self, dzialanie: str, wynik: float):
        wpis = f"{dzialanie} = {wynik}"
        self.historia.append(wpis)
        self.indeks = len(self.historia)-1

    def pokaz(self):
        if not self.historia:
            return "Brak zapisanych dzialan"
        if 0 <= self.indeks < len(self.historia):
            return self.historia[self.indeks]


    def wyczysc(self):
        self.historia.clear()
        self.indeks = -1
        return

    def pokaz_wszystko(self):
        if not self.historia:
            return "Brak zapisanych działań."
        return "\n".join(f"{i + 1}: {wpis}" for i, wpis in enumerate(self.historia))


historia = HistoriaOperacji()

historia.zapisz("2 + 2",4)
historia.zapisz("3 + 5",8)
historia.zapisz("5 + 5",10)
historia.zapisz("2 - 1",1)

print(historia.pokaz())

print(historia.pokaz_wszystko())
historia.wyczysc()
print(historia.pokaz())





'''
zapisz_operacje("2 + 2", 4)
zapisz_operacje("3 + 2", 3)
zapisz_operacje("2 - 1", 2)
pokaz_historie()
'''