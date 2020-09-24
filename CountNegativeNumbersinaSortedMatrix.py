#grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
grid = [[3,2],[1,0]]
#grid=[[8,-2,-2,-2,-4,-5,-5],[-2,-3,-3,-4,-4,-5,-5],[-2,-5,-5,-5,-5,-5,-5],[-3,-5,-5,-5,-5,-5,-5],[-5,-5,-5,-5,-5,-5,-5],[-5,-5,-5,-5,-5,-5,-5],[-5,-5,-5,-5,-5,-5,-5],[-5,-5,-5,-5,-5,-5,-5],[-5,-5,-5,-5,-5,-5,-5]]
cnt=0
for arr in grid:
    ln=len(arr)
    l,r=0,ln-1
    while l<=r:
        mid=(r+l)//2
        print(arr)
        print(l,r,mid,arr[mid])
        if arr[mid]>=0:
            l=mid+1
        elif arr[mid]<0:
            r=mid-1
    if arr[mid]<0:
        cnt+=(ln-mid)
    elif mid+1<ln and arr[mid+1]<0:
            cnt+=(ln-(mid+1))
    print(cnt)
print(cnt)