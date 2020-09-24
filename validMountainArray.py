A=[0,3,2,1]
l=len(A)
cnt=0
i,j=0,1
isUp,isDown = False, False
if l<3:
    print(False)
if A[0]>A[1] or l<3:
    print (False)
while j<l and A[i]<A[j]:
    if A[i]==A[j]:
        print (False)
    cnt+=1
    isUp = True
while j<l and A[i]>A[j]:
    if A[i]==A[j]:
        print (False)
    cnt+=1
    i+=1
    j+=1
    isDown = True
if cnt==l-1 and isUp and isDown:
    print (True)
else:
    print (False)