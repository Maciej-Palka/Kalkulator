from datetime import datetime

"""
Standard zapisu wyników do pliku:
[data czas] działanie = wynik
np. 2025-05-09 12:34:56 2 + 2 = 4
"""

def load_results_from_file(filename="results.txt"):
    results = []
    try:
        with open(filename, "r") as file:
            for line in file:
                line = line.strip()
                if " = " not in line:
                    continue  # pomiń niepoprawne linie

                try:
                    date, time, rest = line.split(" ", 2)
                    expression, result = rest.split(" = ")
                    results.append({
                        "timestamp": f"{date} {time}",
                        "expression": expression.strip(),
                        "result": result.strip()
                    })
                except ValueError:
                    print(f"Błąd parsowania linii: {line}")
                    continue

    except FileNotFoundError:
        print(f"Plik '{filename}' nie istnieje.")
    except Exception as e:
        print(f"Błąd podczas importu: {e}")

    return results