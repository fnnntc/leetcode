class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res=[]
        for i in nums:
            cnt=0
            for j in nums:
                if j<i:
                    cnt+=1
            res.append(cnt)
        return res