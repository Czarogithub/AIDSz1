import time
def partition(t,l,r):
    global counter1, counter2, pivots
    pivots.append(t[l])
    pivot=t[l]
    i=l+1
    j=r
    while True:
        counter2+=2
        while i<=j and t[i]>=pivot:
            counter2+=1
            i+=1
        while t[j]<pivot:
            counter2+=1
            j-=1
        if i>j:
            break
        t[i],t[j]=t[j],t[i]
        counter1+=1
    t[l],t[j]=t[j],t[l]
    counter1+=1
    return j

def quick_sort_i(t):
    start_t=time.perf_counter()
    stack=[(0,len(t)-1)]
    while stack:
        l,r=stack.pop()
        if l<r:
            p=partition(t,l,r)
            stack.append((l,p-1))
            stack.append((p+1,r))
    end_t=time.perf_counter()-start_t
    return [t,end_t]

t=[4,2,5,1,3,2,1,3,2,21,3,1]
t2=t.copy()
pivots=[]
counter1=0;counter2=0
result=quick_sort_i(t)
print(result)
print(f"Czas trwania algorytmu: {result[1]:.6f} sekund")
print(f"Liczba zamian wynosi {counter1}")
print(f"Liczba porównań wynosi {counter2}")
if len(t)<=12:
    print("----------------------------------")
    print("Tryb demonstracyjny")
    print(*t2)
    print(*result[0])
    print(f"Wartości pivota w kolejnych iteracjach {pivots}")