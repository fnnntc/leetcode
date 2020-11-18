nums=[3,1,3]

l,r=0,len(nums)-1
while l<r:
    m=(l+r)//2   
    if nums[l]>=nums[r]:
        l=m+1
    else:
        r=m
print(nums[l])