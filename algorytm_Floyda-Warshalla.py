macierz = [[0,1,5,0,0,0,0],
           [0,0,2,0,0,0,0],
           [0,0,0,0,0,0,0],
           [7,0,0,0,1,0,0],
           [0,0,0,0,0,1,0],
           [2,0,0,4,0,0,0],
           [6,0,0,0,0,3,0]]

d= [[0]* 7 for i in range(7)]
p= [[0]* 7 for i in range(7)]


#wypelnianie d
for i in range (7):
    for j in range (7):
        if i == j:
            d[i][j]=0
        elif macierz[i][j]==0:
            d[i][j]=100
        else:
            d[i][j]=macierz[i][j]

#wypelnianie p
for i in range (7):
    for j in range (7):
        if macierz[i][j]!= 0:
            p[i][j]= i+1
        else:
            p[i][j]= 0

for u in range (7):
    for v in range(7):
        for w in range(7):
            l= d[v][u]+ d[u][w]
            if l< d[v][w]:
                d[v][w]= l
                p[v][w]= p[u][w]

print("d= ")
for i in range (7):
    print(d[i])
print("p=")
for i in range (7):
    print(p[i])