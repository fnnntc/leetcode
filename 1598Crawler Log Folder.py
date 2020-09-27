logs = ["d1/","d2/","../","d21/","./"]
res=0

for i in logs:
    if i=="./":
        continue
    elif i=="../":
        if res>0:
            res-=1
    else:
        res+=1

print(res)