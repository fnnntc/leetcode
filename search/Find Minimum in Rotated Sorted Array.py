nums=[3,4,5,1,2]

l,r=0,len(nums)-1

while l<r:
    m=(l+r)//2   
    if nums[m]>nums[r]:
        l=m+1
    else:
        r=m
else:
    return(nums[l])