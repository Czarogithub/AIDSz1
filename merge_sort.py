import time


def merge_sort(lst):
    start_time = time.perf_counter()
    stats = [0, 0]

    def sort(l):
        if len(l) <= 1:
            return l

        mid = len(l) // 2
        left = sort(l[:mid])
        right = sort(l[mid:])

        stats[1] += 1
        return merge(left, right)

    def merge(left, right):
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            stats[0] += 1
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        while i < len(left):
            result.append(left[i])
            i += 1

        while j < len(right):
            result.append(right[j])
            j += 1

        return result

    sorted_list = sort(lst)
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    return sorted_list, stats[0], execution_time, stats[1]


if __name__ == '__main__':
    my_lst = [38, 27, 43, 3, 9, 82, 10]

    res, comps, merges, duration = merge_sort(my_lst)

    print("Posortowana lista:", res)
    print("Porównania:", comps)
    print("Scalenia:", merges)
    print(f"Czas: {duration:.6f} sek.")