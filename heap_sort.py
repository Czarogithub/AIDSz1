import time


def heapify(lst, x, i, stats):
    max_idx = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < x:
        stats[0] += 1
        if lst[left] < lst[max_idx]:
            max_idx = left

    if right < x:
        stats[0] += 1
        if lst[right] < lst[max_idx]:
            max_idx = right

    if max_idx != i:
        stats[1] += 1
        lst[i], lst[max_idx] = lst[max_idx], lst[i]
        heapify(lst, x, max_idx, stats)


def heap_sort(lst):
    start_time = time.perf_counter()
    x = len(lst)
    stats = [0, 0]

    for i in range(x // 2 - 1, -1, -1):
        heapify(lst, x, i, stats)

    for i in range(x - 1, 0, -1):
        stats[1] += 1
        lst[i], lst[0] = lst[0], lst[i]
        heapify(lst, i, 0, stats)

    end_time = time.perf_counter()
    execution_time = end_time - start_time

    return stats[0], stats[1], execution_time


if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]

    comparisons, swaps, duration = heap_sort(arr)

    print("Sorted array is:", arr)
    print("Liczba porównań:", comparisons)
    print("Liczba zamian:", swaps)
    print("Czas wykonania:", duration, "sekund")