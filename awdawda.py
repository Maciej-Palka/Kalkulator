from collections import deque




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





zapisz_operacje("2 + 2", 4)
zapisz_operacje("3 + 2", 3)
zapisz_operacje("2 - 1", 2)
pokaz_historie()
