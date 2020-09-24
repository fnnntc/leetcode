nums = [-1,0,3,5,9,12]
target = 9

ln=len(nums)
l,r=0,ln-1
while l<=r:
    mid=(r+l)//2
    if target==nums[mid]:
        print("found")
        print(mid)
    elif nums[mid]>target:
        r=mid-1
    elif nums[mid]<target:
        l=mid+1


'''
        print(nums,target)
        l=len(nums)
        left, right = 0, l-1
        while left<=right:
            mid = (left+right)//2
            
            if nums[mid]==target:
                return mid
            
            if nums[mid]>target:
                right=mid-1
            elif nums[mid]<target:
                left=mid+1
        return (-1)'''