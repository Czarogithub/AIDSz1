def merge_sort(lst):
    total_merges = 0
    if len(lst)>1:
        mid_id = len(lst)//2
        l_half = lst[:mid_id]
        r_half = lst[mid_id:]

        l_half, l_merges = merge_sort(l_half)
        r_half, r_merges = merge_sort(r_half)

        total_merges = l_merges + r_merges + 1
        x = y = z = 0
        while x < len(l_half) and y < len(r_half):
            if l_half[x] > r_half[y]:
                lst[z] = l_half[x]
                x+=1
            else:
                lst[z] = r_half[y]
                y += 1
            z += 1

        while x < len(l_half):
            lst[z] = l_half[x]
            x += 1
            z += 1

        while y < len(r_half):
            lst[z] = r_half[y]
            y += 1
            z += 1
    return lst, total_merges

if __name__=='__main__':
    merge_sort.ctr = 0
    my_lst = [38, 27, 43, 3, 9, 82, 10]
    result = merge_sort(my_lst)
    sorted_list = result[0]
    ctr = result[1]
    print(sorted_list, ctr)
