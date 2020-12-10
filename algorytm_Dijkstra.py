def lowest_d(list, k):
    index_min=1
    min=list[1]
    for i in range (1,k):
        if list[i]<= min:
            min= list[i]
            index_min= i
    return index_min

k=5 #ilosc wierzcholkow
Q= [0,1,2,3,4]
d= [100, 100, 100, 100, 100]
p= [0,0,0,0,0]

macierz=[[0, 3, 0, 3, 5],
         [3, 0, 5, 1, 0],
         [0, 5, 0, 2, 0],
         [3, 1, 2, 0, 1],
         [5, 0, 0, 1, 0]]

s=0  #startowy wierzchołek
d[s]=0

for h in range (k):

    if h==s:
        x= 0
    else:
        x= lowest_d(d,k)

    Q[x]= -1

    for i in range (k):
        if macierz[x][i]!= 0:
            if i in Q:
                if d[i]> (d[x]+ macierz[x][i]):
                   d[i]= d[x]+ macierz[x][i]
                   p[i]= x+ 1

print("dist: " +str(d))
print("pred: " +str(p))

