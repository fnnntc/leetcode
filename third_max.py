nums=[2,2,3,2,3,1,2,4,4]
nums=[1,2,2,5,3,5]
#nums=[3,2,1]
nums.sort()
print(nums)
l=len(nums)
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

cnt=0
print("l",l)
if l<3:
    print(max(nums[:l]))

while l>1 and cnt<2:
    print(nums[:l],l,cnt)
    #nums.pop()
    l-=1
    cnt+=1
print(l)
print(max(nums[:l]))