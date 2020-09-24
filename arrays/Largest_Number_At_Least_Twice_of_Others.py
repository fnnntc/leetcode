class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        m=max(nums)
        for i in nums:
            if i!=m:
                if i*2>m:
                    return -1
        return nums.index(m)