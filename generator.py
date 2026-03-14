import random
def data_random(n):
    data=[]
    for i in range(n):
        data.append(random.randint(1,100))
    return data

def data_growing(n):
    data=[]
    a=random.randint(0,8)
    for i in range(n):
        data.append(a)
        a+=random.randint(0,8)
    return data

def data_decreasing(n):
    data=[]
    a=random.randint(1000000,1100000)
    for i in range(n):
        data.append(a)
        a-=random.randint(0,6)
    return data

def data_a(n):
    data=[]
    a=random.randint(n//5*2,n//3*2)
    data+=data_growing(a)
    data += data_decreasing(n-a)
    return data

def data_v(n):
    data=[]
    a=random.randint(n//5*2,n//3*2)
    data+=data_decreasing(a)
    data += data_growing(n-a)
    return data
def generate(n):
    #to do 1 metody
    file = open("data.txt", "w")
    #to do 2 metody
    # dataa = []
    for i in range(10):
        #ten sposób zapisuje ci do pliku data.txt wszystkie ciągi
        # file.write(" ".join(map(str,data_random(n)))+"\n")
        # file.write(" ".join(map(str,data_growing(n)))+"\n")
        # file.write(" ".join(map(str, data_decreasing(n)))+"\n")
        # file.write(" ".join(map(str, data_a(n)))+"\n")
        # file.write(" ".join(map(str, data_v(n)))+"\n")
        #ten sposób zapisuje ci wszystkie ciągi do jednej listy i funkcja generate zwraca tą liste
        # dataa.append(data_random(n))
        # dataa.append(data_growing(n))
        # dataa.append(data_decreasing(n))
        # dataa.append(data_a(n))
        # dataa.append(data_v(n))

    # tu też jedną z 2 linijek wybierz zalezy ktora metode
    file.close()
    # return dataa


print(generate(5))