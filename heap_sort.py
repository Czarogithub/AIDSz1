def heapify(lst, x, i):
    max = i
    left = 2*i+1
    right = 2*i+2

    if left < x and lst[left] < lst[max]:
        max = left

    if right < x and lst[right] < lst[max]:
        max = right

    if max != i:
        lst[i], lst[max] = lst[max], lst[i]
        heapify(lst,x,max)


def heap_sort(lst):
    x = len(lst)

    for i in range(x//2-1, -1, -1):
        heapify(lst,x,i)

    for i in range(x - 1, 0, -1):
        lst[i], lst[0] = lst[0], lst[i]
        heapify(lst, i, 0)


if __name__=='__main__':
    arr = [12, 11, 13, 5, 6, 7]
    heap_sort(arr)
    print("Sorted array is:", arr)