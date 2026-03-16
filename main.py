import generator as gen
import heap_sort as heap
import merge_sort as merge
import qucik_sort_i as quick_i
import quick_sort_rek as quick_r
import shell_sort as shell
import statistics as stats



if __name__=="__main__":
    c = 10 #ILOSC CIAGOW NA RODZAJ
    n = 12 #MAKSYMALNA DLUGOSC CIAGU
    only_one = False #PRZELACZNIK GENERACJI - True - GENERACJA TYLKO DLA N


    limit = 1 if only_one else n
    gen_lsts=[]
    for i in range(limit):
        gen_lsts.extend(gen.generate(c,n if only_one else i+1))

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

    #######################################################################################################
    #CZESC EKSPERYMENTALNA - pomiary
    """
    c=10
    n = 100
    #WZROSTY LINIOWE
    random_lsts=[]
    growing_lsts=[]
    decreasing_lsts=[]
    a_lsts=[]
    v_lsts=[]
    for i in range(10):
        for j in range(c):
            random_lsts.append(gen.data_random(i*n))
            growing_lsts.append(gen.data_growing(i*n))
            decreasing_lsts.append(gen.data_decreasing(i*n))
            a_lsts.append(gen.data_a(i*n))
            v_lsts.append(gen.data_v(i*n))

    with open("line_random_times.txt","w") as random_file:
        time_merge = []
        time_heap = []
        time_shell = []
        time_quick_i = []
        time_quick_r = []

        for lst in random_lsts:
            merge_lst = list(lst)
            merge_res = merge.merge_sort(merge_lst)
            time_merge.append(f'{merge_res[2]:.8f}')

            heap_lst = list(lst)
            heap_res = heap.heap_sort(heap_lst)
            time_heap.append(f'{heap_res[2]:.8f}')

            shell_lst = list(lst)
            shell_res = shell.shell_sort(shell_lst)
            time_shell.append(f'{shell_res[3]:.8f}')

            quick_i_lst = list(lst)
            quick_i_res = quick_i.quick_sort_i(quick_i_lst)
            time_quick_i.append(f'{quick_i_res[3]:.8f}')

            quick_r_lst = list(lst)
            quick_r_res = quick_r.quick_sort_r(quick_r_lst)
            time_quick_r.append(f'{quick_r_res[3]:.8f}')


        print(f'MERGE TIME\n{time_merge}', file=random_file)
        print(f'HEAP TIME\n{time_heap}', file=random_file)
        print(f'SHELL TIME\n{time_shell}', file=random_file)
        print(f'ITERATIVE QUICK TIME\n{time_quick_i}', file=random_file)
        print(f'RECURSIVE QUICK TIME\n{time_quick_r}', file=random_file)

    with open("line_grw_times.txt", "w") as grw_file:
        time_merge = []
        time_heap = []
        time_shell = []
        time_quick_i = []
        time_quick_r = []
        for lst in growing_lsts:
            merge_lst = list(lst)
            merge_res = merge.merge_sort(merge_lst)
            time_merge.append(f'{merge_res[2]:.8f}')

            heap_lst = list(lst)
            heap_res = heap.heap_sort(heap_lst)
            time_heap.append(f'{heap_res[2]:.8f}')

            shell_lst = list(lst)
            shell_res = shell.shell_sort(shell_lst)
            time_shell.append(f'{shell_res[3]:.8f}')

            quick_i_lst = list(lst)
            quick_i_res = quick_i.quick_sort_i(quick_i_lst)
            time_quick_i.append(f'{quick_i_res[3]:.8f}')

            quick_r_lst = list(lst)
            quick_r_res = quick_r.quick_sort_r(quick_r_lst)
            time_quick_r.append(f'{quick_r_res[3]:.8f}')

        print(f'MERGE TIME\n{time_merge}', file=grw_file)
        print(f'HEAP TIME\n{time_heap}', file=grw_file)
        print(f'SHELL TIME\n{time_shell}', file=grw_file)
        print(f'ITERATIVE QUICK TIME\n{time_quick_i}', file=grw_file)
        print(f'RECURSIVE QUICK TIME\n{time_quick_r}', file=grw_file)

    with open("line_dec_times.txt", "w") as dec_file:
        time_merge = []
        time_heap = []
        time_shell = []
        time_quick_i = []
        time_quick_r = []
        for lst in decreasing_lsts:
            merge_lst = list(lst)
            merge_res = merge.merge_sort(merge_lst)
            time_merge.append(f'{merge_res[2]:.8f}')

            heap_lst = list(lst)
            heap_res = heap.heap_sort(heap_lst)
            time_heap.append(f'{heap_res[2]:.8f}')

            shell_lst = list(lst)
            shell_res = shell.shell_sort(shell_lst)
            time_shell.append(f'{shell_res[3]:.8f}')

            quick_i_lst = list(lst)
            quick_i_res = quick_i.quick_sort_i(quick_i_lst)
            time_quick_i.append(f'{quick_i_res[3]:.8f}')

            quick_r_lst = list(lst)
            quick_r_res = quick_r.quick_sort_r(quick_r_lst)
            time_quick_r.append(f'{quick_r_res[3]:.8f}')

        print(f'MERGE TIME\n{time_merge}', file=dec_file)
        print(f'HEAP TIME\n{time_heap}', file=dec_file)
        print(f'SHELL TIME\n{time_shell}', file=dec_file)
        print(f'ITERATIVE QUICK TIME\n{time_quick_i}', file=dec_file)
        print(f'RECURSIVE QUICK TIME\n{time_quick_r}', file=dec_file)

    with open("line_a_times.txt", "w") as a_file:
        time_merge = []
        time_heap = []
        time_shell = []
        time_quick_i = []
        time_quick_r = []
        for lst in a_lsts:
            merge_lst = list(lst)
            merge_res = merge.merge_sort(merge_lst)
            time_merge.append(f'{merge_res[2]:.8f}')

            heap_lst = list(lst)
            heap_res = heap.heap_sort(heap_lst)
            time_heap.append(f'{heap_res[2]:.8f}')

            shell_lst = list(lst)
            shell_res = shell.shell_sort(shell_lst)
            time_shell.append(f'{shell_res[3]:.8f}')

            quick_i_lst = list(lst)
            quick_i_res = quick_i.quick_sort_i(quick_i_lst)
            time_quick_i.append(f'{quick_i_res[3]:.8f}')

            quick_r_lst = list(lst)
            quick_r_res = quick_r.quick_sort_r(quick_r_lst)
            time_quick_r.append(f'{quick_r_res[3]:.8f}')

        print(f'MERGE TIME\n{time_merge}', file=a_file)
        print(f'HEAP TIME\n{time_heap}', file=a_file)
        print(f'SHELL TIME\n{time_shell}', file=a_file)
        print(f'ITERATIVE QUICK TIME\n{time_quick_i}', file=a_file)
        print(f'RECURSIVE QUICK TIME\n{time_quick_r}', file=a_file)

    with open("line_v_times.txt", "w") as v_file:
        time_merge = []
        time_heap = []
        time_shell = []
        time_quick_i = []
        time_quick_r = []
        for lst in v_lsts:
            merge_lst = list(lst)
            merge_res = merge.merge_sort(merge_lst)
            time_merge.append(f'{merge_res[2]:.8f}')

            heap_lst = list(lst)
            heap_res = heap.heap_sort(heap_lst)
            time_heap.append(f'{heap_res[2]:.8f}')

            shell_lst = list(lst)
            shell_res = shell.shell_sort(shell_lst)
            time_shell.append(f'{shell_res[3]:.8f}')

            quick_i_lst = list(lst)
            quick_i_res = quick_i.quick_sort_i(quick_i_lst)
            time_quick_i.append(f'{quick_i_res[3]:.8f}')

            quick_r_lst = list(lst)
            quick_r_res = quick_r.quick_sort_r(quick_r_lst)
            time_quick_r.append(f'{quick_r_res[3]:.8f}')

        print(f'MERGE TIME\n{time_merge}', file=v_file)
        print(f'HEAP TIME\n{time_heap}', file=v_file)
        print(f'SHELL TIME\n{time_shell}', file=v_file)
        print(f'ITERATIVE QUICK TIME\n{time_quick_i}', file=v_file)
        print(f'RECURSIVE QUICK TIME\n{time_quick_r}', file=v_file)

    #WZROSTY WYKŁADNICZE

    random_lsts = []
    growing_lsts = []
    decreasing_lsts = []
    a_lsts = []
    v_lsts = []
    base = 2
    for i in range(10):
        for j in range(c):
            random_lsts.append(gen.data_random((2**(i)) * n))
            growing_lsts.append(gen.data_growing((2**(i)) * n))
            decreasing_lsts.append(gen.data_decreasing((2**(i)) * n))
            a_lsts.append(gen.data_a((2**(i)) * n))
            v_lsts.append(gen.data_v((2**(i)) * n))

    with open("exponent_random_times.txt", "w") as random_file:
        time_merge = []
        time_heap = []
        time_shell = []
        time_quick_i = []
        time_quick_r = []
        for lst in random_lsts:
            merge_lst = list(lst)
            merge_res = merge.merge_sort(merge_lst)
            time_merge.append(f'{merge_res[2]:.8f}')

            heap_lst = list(lst)
            heap_res = heap.heap_sort(heap_lst)
            time_heap.append(f'{heap_res[2]:.8f}')

            shell_lst = list(lst)
            shell_res = shell.shell_sort(shell_lst)
            time_shell.append(f'{shell_res[3]:.8f}')

            quick_i_lst = list(lst)
            quick_i_res = quick_i.quick_sort_i(quick_i_lst)
            time_quick_i.append(f'{quick_i_res[3]:.8f}')

            quick_r_lst = list(lst)
            quick_r_res = quick_r.quick_sort_r(quick_r_lst)
            time_quick_r.append(f'{quick_r_res[3]:.8f}')

        print(f'MERGE TIME\n{time_merge}', file=random_file)
        print(f'HEAP TIME\n{time_heap}', file=random_file)
        print(f'SHELL TIME\n{time_shell}', file=random_file)
        print(f'ITERATIVE QUICK TIME\n{time_quick_i}', file=random_file)
        print(f'RECURSIVE QUICK TIME\n{time_quick_r}', file=random_file)

    with open("exponent_grw_times.txt", "w") as grw_file:
        time_merge = []
        time_heap = []
        time_shell = []
        time_quick_i = []
        time_quick_r = []
        for lst in growing_lsts:
            merge_lst = list(lst)
            merge_res = merge.merge_sort(merge_lst)
            time_merge.append(f'{merge_res[2]:.8f}')

            heap_lst = list(lst)
            heap_res = heap.heap_sort(heap_lst)
            time_heap.append(f'{heap_res[2]:.8f}')

            shell_lst = list(lst)
            shell_res = shell.shell_sort(shell_lst)
            time_shell.append(f'{shell_res[3]:.8f}')

            quick_i_lst = list(lst)
            quick_i_res = quick_i.quick_sort_i(quick_i_lst)
            time_quick_i.append(f'{quick_i_res[3]:.8f}')

            quick_r_lst = list(lst)
            quick_r_res = quick_r.quick_sort_r(quick_r_lst)
            time_quick_r.append(f'{quick_r_res[3]:.8f}')

        print(f'MERGE TIME\n{time_merge}', file=grw_file)
        print(f'HEAP TIME\n{time_heap}', file=grw_file)
        print(f'SHELL TIME\n{time_shell}', file=grw_file)
        print(f'ITERATIVE QUICK TIME\n{time_quick_i}', file=grw_file)
        print(f'RECURSIVE QUICK TIME\n{time_quick_r}', file=grw_file)

    with open("exponent_dec_times.txt", "w") as dec_file:
        time_merge = []
        time_heap = []
        time_shell = []
        time_quick_i = []
        time_quick_r = []
        for lst in decreasing_lsts:
            merge_lst = list(lst)
            merge_res = merge.merge_sort(merge_lst)
            time_merge.append(f'{merge_res[2]:.8f}')

            heap_lst = list(lst)
            heap_res = heap.heap_sort(heap_lst)
            time_heap.append(f'{heap_res[2]:.8f}')

            shell_lst = list(lst)
            shell_res = shell.shell_sort(shell_lst)
            time_shell.append(f'{shell_res[3]:.8f}')

            quick_i_lst = list(lst)
            quick_i_res = quick_i.quick_sort_i(quick_i_lst)
            time_quick_i.append(f'{quick_i_res[3]:.8f}')

            quick_r_lst = list(lst)
            quick_r_res = quick_r.quick_sort_r(quick_r_lst)
            time_quick_r.append(f'{quick_r_res[3]:.8f}')

        print(f'MERGE TIME\n{time_merge}', file=dec_file)
        print(f'HEAP TIME\n{time_heap}', file=dec_file)
        print(f'SHELL TIME\n{time_shell}', file=dec_file)
        print(f'ITERATIVE QUICK TIME\n{time_quick_i}', file=dec_file)
        print(f'RECURSIVE QUICK TIME\n{time_quick_r}', file=dec_file)

    with open("exponent_a_times.txt", "w") as a_file:
        time_merge = []
        time_heap = []
        time_shell = []
        time_quick_i = []
        time_quick_r = []
        for lst in a_lsts:
            merge_lst = list(lst)
            merge_res = merge.merge_sort(merge_lst)
            time_merge.append(f'{merge_res[2]:.8f}')

            heap_lst = list(lst)
            heap_res = heap.heap_sort(heap_lst)
            time_heap.append(f'{heap_res[2]:.8f}')

            shell_lst = list(lst)
            shell_res = shell.shell_sort(shell_lst)
            time_shell.append(f'{shell_res[3]:.8f}')

            quick_i_lst = list(lst)
            quick_i_res = quick_i.quick_sort_i(quick_i_lst)
            time_quick_i.append(f'{quick_i_res[3]:.8f}')

            quick_r_lst = list(lst)
            quick_r_res = quick_r.quick_sort_r(quick_r_lst)
            time_quick_r.append(f'{quick_r_res[3]:.8f}')

        print(f'MERGE TIME\n{time_merge}', file=a_file)
        print(f'HEAP TIME\n{time_heap}', file=a_file)
        print(f'SHELL TIME\n{time_shell}', file=a_file)
        print(f'ITERATIVE QUICK TIME\n{time_quick_i}', file=a_file)
        print(f'RECURSIVE QUICK TIME\n{time_quick_r}', file=a_file)

    with open("exponent_v_times.txt", "w") as v_file:
        time_merge = []
        time_heap = []
        time_shell = []
        time_quick_i = []
        time_quick_r = []
        for lst in v_lsts:
            merge_lst = list(lst)
            merge_res = merge.merge_sort(merge_lst)
            time_merge.append(f'{merge_res[2]:.8f}')

            heap_lst = list(lst)
            heap_res = heap.heap_sort(heap_lst)
            time_heap.append(f'{heap_res[2]:.8f}')

            shell_lst = list(lst)
            shell_res = shell.shell_sort(shell_lst)
            time_shell.append(f'{shell_res[3]:.8f}')

            quick_i_lst = list(lst)
            quick_i_res = quick_i.quick_sort_i(quick_i_lst)
            time_quick_i.append(f'{quick_i_res[3]:.8f}')

            quick_r_lst = list(lst)
            quick_r_res = quick_r.quick_sort_r(quick_r_lst)
            time_quick_r.append(f'{quick_r_res[3]:.8f}')

        print(f'MERGE TIME\n{time_merge}', file=v_file)
        print(f'HEAP TIME\n{time_heap}', file=v_file)
        print(f'SHELL TIME\n{time_shell}', file=v_file)
        print(f'ITERATIVE QUICK TIME\n{time_quick_i}', file=v_file)
        print(f'RECURSIVE QUICK TIME\n{time_quick_r}', file=v_file)
    
    with open("line_statistics.txt", "w") as line_stats:
        input_files = [
            'line_random_times.txt',
            'line_grw_times.txt',
            'line_dec_times.txt',
            'line_a_times.txt',
            'line_v_times.txt'
        ]

        for file_n in input_files:
            print(f'{"#"*100}\n{file_n.split(".")[0]}\n', file=line_stats)
            data_stats=stats.get_stat_arrays(file_n)
            for alg, v in data_stats.items():
                print(f'{alg}\n'
                      f'AVERAGE: {", ".join(v["means"])}\n'
                      f'STD: {", ".join(v["stds"])}'
                      f'\n', file=line_stats)


    with open("exponent_statistics.txt", "w") as exponent_stats:
        input_files = [
            'exponent_random_times.txt',
            'exponent_grw_times.txt',
            'exponent_dec_times.txt',
            'exponent_a_times.txt',
            'exponent_v_times.txt'
        ]

        for file_n in input_files:
            print(f'{"#"*100}\n{file_n.split(".")[0]}\n', file=exponent_stats)
            data_stats=stats.get_stat_arrays(file_n)
            for alg, v in data_stats.items():
                print(f'{alg}\n'
                      f'AVERAGE: {", ".join(v["means"])}\n'
                      f'STD: {", ".join(v["stds"])}'
                      f'\n', file=exponent_stats)
    """



