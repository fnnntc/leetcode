inp = 5
res=[]

res.append([1])
for i in range(inp-1):
    app=[]
    prev=res[i]
    l=len(prev)
    for j in range(l):
        if j==0:
            app.append(1)
        if j+1 <= l-1:
            print(prev[j] + prev[j+1])
            app.append(prev[j] + prev[j+1])
        if j==l-1:
            app.append(1)
    res.append(app)
for f in res:
    print(f)