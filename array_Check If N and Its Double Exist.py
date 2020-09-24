arr = [-10,12,-20,-8,15]

arr.sort()
l=len(arr)
print(arr)
i=0
j=l-1
while i<l:
    while j>i:
        print(arr[i], arr[j])
        if 2*arr[i]==arr[j] or arr[i]==2*arr[j]:
            print("true")
        j-=1
    i+=1
    j=l-1
print("fal")