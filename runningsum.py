nums=[1,2,3,4]

res=[nums[0]]
for i in range (1,len(nums)):
    res.append(nums[i]+res[i-1])

print(res)