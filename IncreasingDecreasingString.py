s = "aaaabbbbcccc"
s=sorted(s)
print(s)
cnt=1
res=''
while s:
    if cnt%2!=0:
        s=sorted(s)
    else:
        s=sorted(s,reverse=True)
    i=''
    c=0
    while c<=(len(s)-1):
        print(c)
        if s[c] not in i:
            i+=s.pop(c)
        else:
            c+=1
    res+=i
    cnt+=1
print(i)
print(res)
print(s)


#cdelotee