class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        nums.sort()
        print(nums)
        l=len(nums)
        if l==0:
            return
        n=l
        print(nums[0])
        #i=nums[0]
        i=1
        res=[]

        cur=0
        nxt=1
        cnt=0

        while nxt<l:
            dist=nxt-cur
            if dist==1 and nums[cur]!=nums[nxt]:
                cur+=1
                nxt+=1
            elif nums[cur]==nums[nxt]:
                nxt+=1
                cnt+=1
            elif dist>1 and nums[cur]!=nums[nxt]:
                nums[cur+1]=nums[nxt]
                #l-=cnt
                #cnt=0
                nxt+=1
                cur+=1
        l-=cnt
        print(nums[:l])

        while i<=n:
            #if nums[i-1]!=i:
            if i not in nums:
                res.append(i)
            i+=1
        return(res)