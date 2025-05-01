from collections import deque




# ilość przechowywaneych działań w pamieci ,
# działania wpisywane w postaci "2 + 2 = 4"
# zapisywanie polega na wpisaniu komendy w poostaci jak w 21 linijce działania i wynik w osobnej
history = deque(maxlen=10)

def zapisz_operacje(dzialanie: str, wynik: float):

    wpis = f"{dzialanie} = {wynik}"
    history.append(wpis)






zapisz_operacje("2 + 2", 4)