nums=[-1,-1,-1,-1,-1,0]

        l=len(nums)
        for i in range(l):
            ls=sum(nums[:i])
            rs=sum(nums[i+1:])
            if ls==rs:
                return(i)
        return(-1)