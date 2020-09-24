A=["cool","lock","cook"]

res = A[0]

for w in A[1:]:
    for c in res:
        if c in w:
            w=w.replace(c,"",1)
        else:
            res=res.replace(c,"",1)

print([x for x in res])
