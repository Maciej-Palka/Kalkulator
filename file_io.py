from datetime import datetime

"""
Standard zapisu wyników do pliku:
[data czas] działanie = wynik
np. 2025-05-09 12:34:56 2 + 2 = 4
"""

def save_results_to_file(results, filename="results.txt"):
    try:
        with open(filename, "w") as file:
            for item in results:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                file.write(f"{timestamp} {item['expression']} = {item['result']}\n")
    except IOError as e:
        print(f"Błąd zapisu do pliku: {e}")


def load_results_from_file(filename="results.txt"):
    results = []
    try:
        with open(filename, "r") as file:
            for line in file:
                line = line.strip()
                if " = " in line:
                    # Rozbij linię na część: data czas, wyrażenie, wynik
                    date, time, rest = line.split(" ", 2)
                    expression, result = rest.split(" = ")
                    results.append({
                        "timestamp": f"{date} {time}",
                        "expression": expression.strip(),
                        "result": result.strip()
                    })
    except FileNotFoundError:
        print("Plik nie istnieje.")
    except Exception as e:
        print(f"Błąd podczas importu: {e}")
    return results
