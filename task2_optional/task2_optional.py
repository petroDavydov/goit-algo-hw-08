import heapq
from colorama import Fore, Style, init
init(autoreset=True)

def merge_k_lists(lists):
    min_heap = []

    # Додаємо перші елементи кожного списку в купу
    for i in range(len(lists)):
        if lists[i]:  # Перевіряємо, чи список не порожній
            heapq.heappush(min_heap, (lists[i][0], i, 0))  # (значення, індекс списку, індекс елемента)
            print(f"{Fore.LIGHTGREEN_EX}Додано в купу: (значення={lists[i][0]}, список={i}, індекс=0){Style.RESET_ALL}")

    merged_list = []

    # Поки купа не порожня
    while min_heap:
        # Витягуємо найменший елемент
        val, list_idx, elem_idx = heapq.heappop(min_heap)
        print(f"{Fore.LIGHTYELLOW_EX}Витягнуто з купи: (значення={val}, список={list_idx}, індекс={elem_idx}){Style.RESET_ALL}")
        merged_list.append(val)

        # Якщо в списку є ще елементи, додаємо наступний елемент у купу
        if elem_idx + 1 < len(lists[list_idx]):
            next_value = lists[list_idx][elem_idx + 1]
            next_tuple = (next_value, list_idx, elem_idx + 1)
            heapq.heappush(min_heap, next_tuple)
            print(f"{Fore.LIGHTBLUE_EX}Додано в купу: (значення={next_value}, список={list_idx}, індекс={elem_idx + 1}){Style.RESET_ALL}")

    print(f"{Style.BRIGHT}{Fore.CYAN}Злиття завершено. Відсортований список: {Fore.RED}{merged_list}{Style.RESET_ALL}")
    return merged_list

# Приклад використання
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print(f"{Style.DIM}Відсортований список:{Fore.LIGHTBLUE_EX} {merged_list}{Style.RESET_ALL}")