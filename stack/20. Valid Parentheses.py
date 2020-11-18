s ="())"
o = ["(","[","{"]
c = [")","]","}"]
valid = []

for i in s:
    if i in o:
        valid.append(i)
    elif i in c:
        if not valid or o.index(valid.pop()) != c.index(i):
            print(False)
            break
if valid:
    print(False)

print(True)


"""s ="([]){"
s=list(s)
print(s)
o = ["(","[","{"]
c = [")","]","}"]
valid = []
res=False
while s:
    k=s.pop(0)
    if k in o:
        valid.append(k)
    elif k in c and valid:
        if o.index(valid.pop()) == c.index(k):
            res=True
        else:
            res=False
            break
    else:
        res=False
if valid:
    print(False)
print(res)"""