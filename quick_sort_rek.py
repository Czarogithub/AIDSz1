import time
def Partition(t,p,r):
    global counter1,counter2,pivots
    counter1+=1
    pivots.append(t[p])
    t[p],t[r]=t[r],t[p]
    x=t[r]
    i=p
    j=r
    while True:
        counter2+=2
        while i<=r and t[i]>x:
            i+=1
            counter2+=1
        while t[j]<x:
            j-=1
            counter2+=1
        if i <=j:
            t[i],t[j]=t[j],t[i]
            counter1+=1
            i+=1
            j-=1
        else:
            return j

def quick_sort_r(t,p,r,end_t):
    start_t = time.perf_counter()
    if p<r:
        q=Partition(t,p,r)
        quick_sort_r(t,p,q,end_t)
        quick_sort_r(t,q+1,r,end_t)
    end_t += time.perf_counter()-start_t
    return [t,end_t]


t=[4,2,5,1,3,2,1,3,2,21,3,1]
t2=t.copy()
pivots=[]
end_t=0;counter1=0;counter2=0
result=quick_sort_r(t,0,len(t)-1,end_t)
print(f"Czas trwania algorytmu: {result[1]:.6f} sekund")
print(f"Liczba zamian wynosi {counter1}")
print(f"Liczba porównań wynosi {counter2}")
if len(t)<=12:
    print("----------------------------------")
    print("Tryb demonstracyjny")
    print(*t2)
    print(*result[0])
    print(f"Wartości pivota w kolejnych iteracjach {pivots}")