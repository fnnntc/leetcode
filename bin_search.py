class Solution:
    def search(self, nums: [int], target: int) -> int:
        print(nums,target)
        l=len(nums)
        left,right = 0, l-1
        
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                print(nums[mid], mid)
                return ()
            if nums[mid]>target:
                right=mid-1
            elif nums[mid]<target:
                left=mid+1
        

nums = [-1,0,3,5,9,12,13]
target = -1
Solution.search(nums, nums,target)