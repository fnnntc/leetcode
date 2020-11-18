n=3
bad=2

def isBadVersion(x):
    if x==2:
        return(True)

"""
l,r=1,n
versions = {}

if len(nums)==0:
    return (-1)

while l<r:
    m = (l+r)//2

    isBad = isBadVersion(m)
    if not isBad and m+1 in versions:
        if versions[m+1]==True:
            print(m+1)
    elif isBad and l==n:
        print(l)
    elif isBad:
        versions[m]=True
        r=m
        if m==1:
            print(m)
        if m-1 in versions:
            if versions[m-1]==False:
                print(m)
    elif not isBad:
        versions[m]=False
        l=m+1
if l==n and isBadVersion(l):
    print(l)

print(-1)"""
l,r=1,n
while l<r:
    m=(l+r)//2
    isBad=isBadVersion(m)
    if not isBad:
        l=m+1
    else:
        r=m
print(l)