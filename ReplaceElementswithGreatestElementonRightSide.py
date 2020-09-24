## Replace Elements with Greatest Element on Right Side

arr = [17,18,5,4,6,1]

i=0
l=len(arr)
while i<l-1:
    m=max(arr[i+1:])
    arr[i]=m
    i+=1
arr[l-1]=-1
print(arr)