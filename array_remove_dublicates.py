nums = [-50,-50,-49,-49,-48,-46,-45,-45,-43,-42,-38,-35,-35,-32,-32,-31,-30,-29,-26,-26,-25,-24,-24,-23,-23,-23,-23,-22,-22,-21,-19,-17,-17,-17,-17,-16,-16,-15,-13,-11,-9,-9,-9,-8,-8,-7,-7,-5,-3,-2,-2,0,0,4,5,5,6,6,7,10,10,10,10,11,11,12,13,14,15,15,15,15,15,15,18,19,20,20,25,26,26,27,27,29,29,29,31,31,33,33,33,33,33,34,35,35,36,37,38,39,39,39,39,43,43,46,48,50,50]
#nums=[5,6,7,7,7,7,8,8,9,9,9]
#nums=[1,1,1,1,2,2,2,3]
l=len(nums)
#print(l)
#i=0
#j=0
#if l==1:
#    return
'''
while i<l-1:
    if nums[i]==nums[i+1]:
        j=i+1
        while j<l:
            nums[j-1]=nums[j]
            j+=1
        l-=1
    if nums[i]!=nums[i+1]:
        i+=1
print(nums[:l])'''

'''while i<l-1:
    k=0
    if nums[i]==nums[i+1]:
        cnt=0
        k=i+1
        j=i+1
        while k<l and nums[k]==nums[i]:
            cnt+=1
    #        print(nums[i],i,k,cnt,l) 
            k+=1
    #    print(nums)    
        while j+cnt<l:
            nums[j]=nums[j+cnt]
            j+=1
    #       print(nums, i, j, l)
        l-=cnt
    #print("qq")
    #print(nums[i],nums[i+1],i,l)
    if nums[i]!=nums[i+1]:    
        i+=1
    #print(i,l)
print(nums[:l])'''

'''
cur=0
nxt=1
print(nums)
while nxt < len(nums):
    cnt=1
    dist = abs(cur - nxt)
    if dist == 1 and nums[cur]!=nums[nxt]:
        cur += 1
        nxt += 1
    elif dist >1 and nums[cur] < nums[nxt]:
        nums[cur+1] = nums[nxt]
        l -= 1
        cur += 1
        print(nums[:l])
    #elif dist>1 and nums[cur] == nums[nxt]:
    #    nxt += 1
    else: 
        nxt+=1
        #l-=1
print("final")
print(l)
print(nums)
print(nums[:l])
'''

cur=0
nxt=1
cnt=0
print(nums)
while nxt < len(nums):
    dist = abs(cur - nxt)
    if dist==1 and nums[cur]!=nums[nxt]:
        nxt+=1
        cur+=1    
    elif nums[cur]==nums[nxt]:
        cnt+=1
        nxt+=1
    elif dist>1 and nums[cur]!=nums[nxt]:
        nums[cur+1]=nums[nxt]
        print(l,cnt)
        l-=cnt
        cnt=0
        nxt+=1
        cur+=1
if cnt>0:
    l-=cnt
return(nums)
print(nums[:l])
