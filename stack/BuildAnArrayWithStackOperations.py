target=[2,3,4]
n = 4

m = target[-1]
res = []
for i in range(1,m+1):
    res.append("Push")
    if i not in target:
        res.append("Pop")

print(res)