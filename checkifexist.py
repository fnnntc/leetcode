arr=[-2,0,10,-19,4,6,-8,8]
arr.sort()
print(arr)
l=len(arr)
for i in range(l):
    for j in range(l-1,i,-1):
        if arr[i]*2==arr[j] or arr[i]==arr[j]*2:
            print(arr[i])
    