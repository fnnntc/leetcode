nums = [4,3,10,9,8]
nums.sort(reverse=True)
ls,rs=0,sum(nums)
#print(nums,ls,rs)
for i in range(len(nums)):
    ls=sum(nums[:i])
    rs=sum(nums[i:])
    if ls>rs:
        return(nums[:i])
return(nums)    