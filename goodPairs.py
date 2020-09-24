nums = [1,2,3,1,1,3]

cnt=0
l=len(nums)
for i in range(l-1):
    for j in range(i+1,l):
        if nums[i]==nums[j]:
            print(i,j)
            cnt+=1
print(cnt)