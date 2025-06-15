import heapq
from colorama import Fore, Style, init
init(autoreset=True)


def min_cost_connect_cable(cable_length):
    # Сворення купи використовуючи список довжини кабелів
    heapq.heapify(cable_length)
    total_cost = 0

    # Перебираємо купу поки > 1 кабеля
    while len(cable_length) > 1:
        first = heapq.heappop(cable_length)
        second = heapq.heappop(cable_length)

        # Витрати на з'єднання
        cost = first + second
        total_cost += cost

        # + новий кабель до купи
        heapq.heappush(cable_length, cost)

        print(
            f"Об'єнюємо кабелі {Fore.BLUE}{first} та {Fore.BLUE}{second} получаємо витрати {Fore.LIGHTYELLOW_EX}{cost}. \n Загальні витрати --> {Fore.RED}{total_cost}{Style.RESET_ALL}")

        print(f"Стан купи на зараз: {Fore.LIGHTCYAN_EX}{cable_length}{Style.RESET_ALL}")

    return total_cost


if __name__ == "__main__":

    cable_lengths = [10, 23, 34, 1, 27, 5, 9, 99, 123, 90, 4]
    minimum_cost = min_cost_connect_cable(cable_lengths)
    print(f"{Fore.LIGHTWHITE_EX}Мінімальні витрати на об'єднання кабелів: \n {Fore.LIGHTGREEN_EX}{minimum_cost}{Style.RESET_ALL}")
