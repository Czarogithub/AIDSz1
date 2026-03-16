import generator as gen
import heap_sort as heap
import merge_sort as merge
import qucik_sort_i as quick_i
import quick_sort_rek as quick_r
import shell_sort as shell

if __name__=="__main__":
    c = 1 #ILOSC CIAGOW NA RODZAJ
    n = 12 #MAKSYMALNA DLUGOSC CIAGU
    only_one = True #PRZELACZNIK GENERACJI - True - GENERACJA TYLKO DLA N


    limit = 1 if only_one else n
    gen_lsts=[]
    for i in range(limit):
        gen_lsts.extend(gen.generate(c,n))\

    x = 1
    with open('results.txt',"w") as results:
        for lst in gen_lsts:
            print(f'{"#"*100}\n{x}. LISTA NIEPOSORTOWANA: {lst}\n', file=results)
            x+=1

            heap_lst = list(lst)
            heap_res = heap.heap_sort(heap_lst)
            print(f'HEAP SORT'
                  f'\n'
                  f'posortowana lista: {heap_lst}\n'
                  f'liczba porownan: {heap_res[0]}\n'
                  f'liczba zmian: {heap_res[1]}\n'
                  f'czas algorytmu: {heap_res[2]:.6f} sek.\n', file = results)


            merge_lst = list(lst)
            merge_res = merge.merge_sort(merge_lst)
            print(f'MERGE SORT'
                  f'\n'
                  f'posortowana lista: {merge_res[0]}\n'
                  f'liczba porownan: {merge_res[1]}', file = results)
            if len(merge_lst)<=12:
                  print(f'liczba scalen: {merge_res[3]}', file = results)
            print(f'czas algorytmu: {merge_res[2]:.6f} sek.\n', file = results)

            shell_lst = list(lst)
            shell_res = shell.shell_sort(shell_lst)
            print(f'SHELL SORT'
                  f'\n'
                  f'posortowana lista: {shell_res[0]}\n'
                  f'liczba porownan: {shell_res[1]}\n'
                  f'liczba zamian elementow: {shell_res[2]}', file = results)
            if len(shell_lst)<=12:
                  print(f'wartosci przyrostu knutha: {shell_res[4]}', file = results)
            print(f'czas algorytmu: {shell_res[3]:.6f} sek.\n', file = results)

            quick_i_lst = list(lst)
            quick_i_res = quick_i.quick_sort_i(quick_i_lst)
            print(f'ITERATIVE QUICK SORT'
                  f'\n'
                  f'posortowana lista: {quick_i_res[0]}\n'
                  f'liczba porownan: {quick_i_res[1]}\n'
                  f'liczba zamian elementow: {quick_i_res[2]}', file=results)
            if len(quick_i_lst) <= 12:
                print(f'wartosci pivota: {quick_i_res[4]}', file=results)
            print(f'czas algorytmu: {quick_i_res[3]:.6f} sek.\n', file=results)

            quick_r_lst = list(lst)
            quick_r_res = quick_r.quick_sort_r(quick_r_lst)
            print(f'RECURSIVE QUICK SORT'
                  f'\n'
                  f'posortowana lista: {quick_r_res[0]}\n'
                  f'liczba porownan: {quick_r_res[1]}\n'
                  f'liczba zamian elementow: {quick_r_res[2]}', file=results)
            if len(quick_i_lst) <= 12:
                print(f'wartosci pivota: {quick_r_res[4]}', file=results)
            print(f'czas algorytmu: {quick_r_res[3]:.6f} sek.\n', file=results)






