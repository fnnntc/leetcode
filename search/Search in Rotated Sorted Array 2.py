nums = [4,5,6,7,0,1,2]
target =2 


l, r = 0, len(nums) -1
while l <= r:
    m = (l + r)//2
    if nums[m] == target:
        print(m)
        break
    elif nums[m] > nums[r]:
        l = m + 1
    else:
        r = m - 1
else:
    l,r = 0, len(nums) - 1
    while l <= r:
        m = (l + r)//2
        if nums[m] == target:
            print(m)
        elif nums[m] < target:
            l = m + 1
        else:
            r = m - 1

print(-1)