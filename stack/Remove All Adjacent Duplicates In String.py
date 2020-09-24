s="abbaca"
i,l,res=0,len(s),[]
while i<l:
    res.append(s[i])
    print(res)
    if len(res)>1:
        if res[-1]==res[-2]:
            res.pop()
            res.pop()
    i+=1

print("".join(res))