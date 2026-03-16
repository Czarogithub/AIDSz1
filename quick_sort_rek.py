import time


def Partition(t, p, r, stats):
    stats[0] += 1
    stats[2].append(t[p])
    t[p], t[r] = t[r], t[p]
    x = t[r]
    i = p
    j = r
    while True:
        while i <= r:
            stats[1] += 1
            if t[i] > x:
                i += 1
            else:
                break
        while j >= p:
            stats[1] += 1
            if t[j] < x:
                j -= 1
            else:
                break
        if i <= j:
            t[i], t[j] = t[j], t[i]
            stats[0] += 1
            i += 1
            j -= 1
        else:
            return j


def quick_sort_r(t):
    start_t = time.perf_counter()

    stats = [0, 0, []]

    def _quick_sort(t, p, r):
        if p < r:
            q = Partition(t, p, r, stats)
            _quick_sort(t, p, q)
            _quick_sort(t, q + 1, r)

    _quick_sort(t, 0, len(t) - 1)

    end_t = time.perf_counter() - start_t

    return t, stats[0], stats[1], end_t, stats[2]


if __name__ == "__main__":
    t = [4, 2, 5, 1, 3, 2, 1, 3, 2, 21, 3, 1]
    t2 = t[:]

    res_list, swaps, comps, duration, p_list = quick_sort_r(t)

    print(f"Czas trwania algorytmu: {duration:.6f} sekund")
    print(f"Liczba zamian wynosi {swaps}")
    print(f"Liczba porównań wynosi {comps}")

    if len(t2) <= 12:
        print("----------------------------------")
        print("Tryb demonstracyjny")
        print("Oryginalna:", *t2)
        print("Posortowana:", *res_list)
        print(f"Pivoty: {p_list}")