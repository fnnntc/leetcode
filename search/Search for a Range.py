nums = [1,3]

target = 1

if len(nums) == 0:
    print -1

l, r = 0, len(nums) - 1
start,end=-1,-1



while l+1 < r:
    mid = (l+r)//2
    if nums[mid] == target and nums[mid-1] < target:
        start = mid
        break
    elif nums[mid] < target:
        l = mid
    else:
        r = mid
    
if nums[l] == target: start= l

print(start,end)


l, r = 0, len(nums) - 1
while l+1 < r:
    mid = (l+r)//2
    if nums[mid] == target and nums[mid+1] > target:
        end = mid
        break
    elif nums[mid] > target:
        r = mid
    else:
        l = mid


if nums[r] == target: end= r

print(start,end)