import time


def partition(t, l, r, stats):
    pivots = stats[2]
    pivots.append(t[l])
    pivot = t[l]
    i = l + 1
    j = r

    while True:
        while i <= j:
            stats[1] += 1  # Porównanie i <= j
            if t[i] >= pivot:
                i += 1
            else:
                break

        while j >= l:
            stats[1] += 1  # Porównanie t[j] < pivot
            if t[j] < pivot:
                j -= 1
            else:
                break

        if i > j:
            break

        t[i], t[j] = t[j], t[i]
        stats[0] += 1  # Zamiana

    t[l], t[j] = t[j], t[l]
    stats[0] += 1  # Zamiana końcowa z pivotem
    return j


def quick_sort_i(t):
    start_t = time.perf_counter()

    # stats: [zamiany, porównania, lista_pivotów]
    stats = [0, 0, []]
    stack = [(0, len(t) - 1)]

    while stack:
        l, r = stack.pop()
        if l < r:
            p = partition(t, l, r, stats)
            stack.append((l, p - 1))
            stack.append((p + 1, r))

    end_t = time.perf_counter() - start_t

    # Zwracamy wszystko jako jeden zestaw wyników
    return t, stats[1], stats[0], end_t, stats[2]


if __name__ == "__main__":
    arr = [4, 2, 5, 1, 3, 2, 1, 3, 2, 21, 3, 1]

    # Teraz wywołanie jest czyste - nie musisz zerować globalnych zmiennych
    sorted_list, swaps, comps, duration, p_list = quick_sort_i(arr)

    print(f"Posortowana: {sorted_list}")
    print(f"Zamiany: {swaps}, Porównania: {comps}")
    print(f"Pivoty: {p_list}")