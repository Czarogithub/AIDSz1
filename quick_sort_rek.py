import time


def Partition(t, p, r, stats):
    mid = (p + r) // 2
    t[mid], t[r] = t[r], t[mid]

    pivot = t[r]
    stats[2].append(pivot)
    i = p - 1

    for j in range(p, r):
        stats[1] += 1
        if t[j] <= pivot:
            i += 1
            t[i], t[j] = t[j], t[i]
            stats[0] += 1

    t[i + 1], t[r] = t[r], t[i + 1]
    stats[0] += 1
    return i + 1


def quick_sort_r(t):
    start_t = time.perf_counter()
    stats = [0, 0, []]

    def _quick_sort(t, p, r):
        if p < r:
            q = Partition(t, p, r, stats)
            _quick_sort(t, p, q - 1)
            _quick_sort(t, q + 1, r)

    _quick_sort(t, 0, len(t) - 1)

    end_t = time.perf_counter() - start_t
    return t, stats[0], stats[1], end_t, stats[2]


if __name__ == "__main__":
    t = [i for i in range(1500)]
    t2 = t[:]

    res_list, swaps, comps, duration, p_list = quick_sort_r(t)

    print(f"Czas trwania: {duration:.6f} s")
    print(f"Zamiany: {swaps}, Porównania: {comps}")