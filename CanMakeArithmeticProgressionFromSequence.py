arr = [3,5,1]
arr.sort()
d=arr[1]-arr[0]
print(arr)
for i in range(len(arr)-1):
    if arr[i+1]-arr[i]!=d:
        print("False")