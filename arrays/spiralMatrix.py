S=[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

res=[]
i,j=0,0
l=len(S[0])

while j <= l-1:
    res.append(S[i][j])
    j+=1
i+=1
while i<= l-1:
    res.append(S[i][j])
    i+=1
i-=1
while j >= 0:
    res.append(S[i][j])
    i-=1

print(res)