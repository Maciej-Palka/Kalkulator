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
    pass  # do zaimplementowania później