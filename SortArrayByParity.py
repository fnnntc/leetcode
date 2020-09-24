A = [3,1,2,4]
#Output: [2,4,3,1]
i=0
j=1
l=len(A)

while j<l:
    if A[i]%2!=0 and A[j]%2==0:
        tmp=A[j]
        A[j]=A[i]
        A[i]=tmp
    elif A[i]%2!=0 and A[j]!=0:
        j+=1
    elif A[i]%2==0:
        i+=1
        j+=1
print(A)

