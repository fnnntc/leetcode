'''Given n and m which are the dimensions of a matrix initialized by zeros and given an array indices where indices[i] = [ri, ci]. For each pair of [ri, ci] you have to increment all cells in row ri and column ci by 1.

Return the number of cells with odd values in the matrix after applying the increment to all indices.
 '''

n = 2
m = 3
indices = [[0,1],[1,1]]
cnt=0

mx= [[0]*m for i in range(n)]

for i in indices:
    for r in range(m):
        mx[i[0]][r]+=1
    for c in range(n):
        mx[c][i[1]]+=1
for arr in mx:
    for el in arr:
        if el%2!=0:
            cnt+=1
print(mx)
print(cnt)