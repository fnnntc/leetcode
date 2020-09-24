nums = [0,1,0,3,12]

l=len(nums)
i=0
j=1
cnt=0

while j < l:
    if nums[i]==0 and nums[j]!=0:
        nums[i]=nums[j]
        nums[j]=0
        i+=1
        j+=1
    elif nums[i]==0 and nums[j]==0:
        j+=1
    elif nums[i]!=0:
        i+=1
        j+=1

    
print(nums)