macierz=[[0, 3, 0, 3, 5],
         [3, 0, 5, 1, 0],
         [0, 5, 0, 2, 0],
         [3, 1, 2, 0, 1],
         [5, 0, 0, 1, 0]]
v= 5
k= [0, 100, 100, 100, 100]
pred= [0, 0, 0, 0, 0]
low_key= k[2]

for i in range (v):
    for j in range (v):
        if macierz[i][j]!= 0:
            if  macierz[i][j]< k[j]:
                if macierz[i][j]< low_key:
                    low_key= j
                k[j]= macierz[i][j]
                pred[j]= i+1
                for l in range (v):
                    macierz[low_key][l]= 0
                    macierz[l][low_key]= 0

print("pred: " + str(pred))
print("k: " + str(k))