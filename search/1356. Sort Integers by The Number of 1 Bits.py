import math
arr = [1024,512,256,128,64,32,16,8,4,2,1]
arr.sort()
m=max(arr)
x=(int(math.log(m,2)))

new =[]

for c in range (x+1) :
    for i in arr:
        if "{0:b}".format(i).count("1")==c:
            new.append(i)
print(new)