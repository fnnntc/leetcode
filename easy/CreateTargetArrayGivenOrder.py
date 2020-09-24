nums = [0,1,2,3,4]
index = [0,1,2,2,1]
l=len(nums)
res=[0]*l
for i in range(l):
    res=res[:index[i]]+[nums[i]]+res[index[i]:l-1]

print(res)