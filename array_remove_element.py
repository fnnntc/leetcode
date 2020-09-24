nums = [3,2,2,3]
val=3
l=len(nums)
#for i in range(1,l):
 #   nums[i-1]=nums[i]
#l-=1
#print(nums[:l])
'''
for i in range(l):
    if nums[i]==val:
        print(i,nums[i])
        for j in range(i+1,l):
            nums[j-1]=nums[j]
        l-=1
    print(nums)
'''
i=0
j=0
while i<l:
    if nums[i]==val:
        print(i,nums[i])
        #for j in range(i+1,l):
        j=i+1
        while j<l:
            nums[j-1]=nums[j]
            j+=1
        l-=1
    if nums[i]!=val:
        i+=1
print(nums[:l])