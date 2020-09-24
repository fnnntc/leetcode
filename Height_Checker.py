heights = [1,1,4,2,1,3]
cnt=0
h=sorted(heights)
for i in range (len(heights)):
    if heights[i]!=h[i]:
        cnt+=1
print(cnt)