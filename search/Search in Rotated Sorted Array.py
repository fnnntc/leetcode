nums = [1,2,3,4]
target = 4

def search(nums, target):
    i=0
    while nums[i]>nums[i-1]:
        i+=1
    print(i)
    l,r=0,i
    while l<=r:
        m=(l+r)//2
        if nums[m]<target:
            l=m+1
        elif nums[m]>target:
            r=m-1
        else:
            return(m)
    else:
        l,r=i,len(nums)-1
        while l<=r:
            m=(l+r)//2
            if nums[m]<target:
                l=m+1
            elif nums[m]>target:
                r=m-1
            else:
                return(m)
    return (-1)
        

print(search(nums,target))