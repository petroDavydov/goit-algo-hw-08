import heapq
from colorama import Fore, Style, init
init(autoreset=True)


def merge_k_lists(lists):

    min_heap = []

    for i in range(len(lists)):
        if lists[i]:
            heapq.heappush(min_heap, (lists[i][0], i, 0))

    merged_list = []

    while min_heap:
        val, list_idx, elem_idx = heapq.heappop(min_heap)
        merged_list.append(val)

        if elem_idx + 1 < len(lists[list_idx]):
            next_tuple = (lists[list_idx][elem_idx + 1], list_idx, elem_idx+1)
            heapq.heappush(min_heap, next_tuple)

    return merged_list


lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print(f"{Fore.CYAN}Відсортований список:  \n {Fore.LIGHTRED_EX}{merged_list}{Style.RESET_ALL}")

# Відсортований список: [1, 1, 2, 3, 4, 4, 5, 6]
