nums = [3,1]
target = 3


l=len(nums)
left, right = 0, l-1

st_pos=0
for i in range(l-1):
    if nums[i]>nums[i+1]:
        st_pos=i+1

#st_pos = nums.index(0)
tmp=nums[st_pos:]+nums[:st_pos]
print(tmp)
if st_pos>0:
    nums=tmp

while left<=right:
    mid=(left+right)//2

    if nums[mid]==target:
        print(nums[mid],st_pos)
        break
    
    if nums[mid]<target:
        left=mid+1
    elif nums[mid]>target:
        right=mid-1
print(-1)