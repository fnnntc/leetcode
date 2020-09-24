s="(()())(())"
s=list(s)
res=[]
T=s.pop()
while s:
    T2=s.pop()
    if T==")" and T2=="(":
        res.append(T2)
        res.append(T)
    T=T2
print("".join(res))