a=[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

cur=0
for i in range(3):
    if cur==0:
        while cur<=i:
            print(a[cur][i-1])
            cur=+1
            i=-1
    elif cur==i:
        while cur>=0:
            print(a[cur][i-1])
            cur=-1
            i=+1