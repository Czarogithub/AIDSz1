import time
# def insertion_sort(t):
#     for j in range(2,len(t)):
#         key = t[j]
#         i = j-1
#         while i >= 0 and t[i] < key:
#             t[i+1] = t[i]
#             i = i-1
#         t[i+1] = key
#     return t


def shell_sort(t):
    start_t = time.perf_counter()
    counter1 = 0;counter2 = 0
    n=len(t)
    knuth=[]
    h=1
    while h<n//3:
        h=3*h+1

    while h >= 1:
        knuth.append(h)
        for j in range(h,n):
            key=t[j]
            i=j-h
            counter2+=1
            while i>=0 and t[i]<key:
                counter2+=1
                counter1+=1
                t[i+h]=t[i]
                i=i-h
            t[i+h]=key
        h=h//3
    end_t = time.perf_counter()
    #print(f"Czas trwania algorytmu: {end_t-start_t:.6f} sekund")
    execution_time = end_t-start_t
    return t,counter2,counter1,execution_time,knuth

if __name__=="__main__":
    t=[4,2,5,1,3,2,1,3,2,2,2,21,3,1]
    result=shell_sort(t)
    print(result[0])
    print(f"Liczba zamian wynosi {result[1]}")
    print(f"Liczba porównań wynosi {result[2]}")
    if len(t)<=12:
        print("Tryb demonstracyjny")
        print(f"Wartość przyrostu w kolejnych iteracjach {result[3]}")







#shell sort git



