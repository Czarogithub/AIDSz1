import time


def partition(t, l, r, stats):
    mid = (l + r) // 2
    t[mid], t[l] = t[l], t[mid]
    stats[0] += 1

    pivot = t[l]
    stats[2].append(pivot)

    i = l
    j = r + 1

    while True:
        i += 1
        while i <= r:
            stats[1] += 1
            if t[i] < pivot:
                i += 1
            else:
                break

        j -= 1
        while j >= l:
            stats[1] += 1
            if t[j] > pivot:
                j -= 1
            else:
                break

        if i >= j:
            break

        t[i], t[j] = t[j], t[i]
        stats[0] += 1

    t[l], t[j] = t[j], t[l]
    stats[0] += 1
    return j


def quick_sort_i(t):
    start_t = time.perf_counter()
    stats = [0, 0, []]

    if len(t) > 1:
        stack = [(0, len(t) - 1)]
        while stack:
            l, r = stack.pop()

            if l < r:
                p = partition(t, l, r, stats)

                if (p - l) > (r - p):
                    stack.append((l, p - 1))
                    stack.append((p + 1, r))
                else:
                    stack.append((p + 1, r))
                    stack.append((l, p - 1))

    end_t = time.perf_counter() - start_t
    return t, stats[1], stats[0], end_t, stats[2]


if __name__ == "__main__":
    arr = [4, 2, 5, 1, 3, 2, 1, 3, 2, 21, 3, 1]
    sorted_list, comps, swaps, duration, p_list = quick_sort_i(arr)

    print(f"Posortowana: {sorted_list}")
    print(f"Porownania: {comps}, Zamiany: {swaps}")
    print(f"Pivoty: {p_list}")
    print(f"Czas: {duration:.6f} s")