A=["cool","lock","cook"]
res=[]
for c in A[0]:
    res.append(c)


for c in range(len(res)):
    isAll=False
    for w in A:
        if c in w:
            isAll=True
        else:
            res.pop(res.index(c))
            isAll=False