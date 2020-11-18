
nums=[5,4]
nums=[5]
nums=[4,5]
#nums=[1,2,3,4,3]

l,r=0,len(nums)-1

while l<r:
    m=(l+r)//2
    if nums[m]>nums[m+1]:
        r=m
    else:
        l=m+1
else:
    print(l)
