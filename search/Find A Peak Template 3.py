nums = [3,3,3]



def findPeakElement(nums):
    l,r=0, len(nums)-1
    while l+1 < r:
        mid=(l+r)//2
        if nums[mid-1]<nums[mid] and nums[mid]>nums[mid+1]:
            return(nums[mid])
        elif nums[mid]<nums[mid+1]:
            l=mid
        else:
            r=mid

    if nums[l]>nums[r]: return nums[l]
    if nums[r]>nums[l]: return nums[r]
    return -1
print(findPeakElement(nums))