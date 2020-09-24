from collections import Counter

nums1 = [1,2,2,1]
nums2 = [2]

#intersection 1
#s1,s2 = set(nums1),set(nums2)
#print(set.intersection(s1,s2))

#intersection 2

res=[]
for n in range (len(nums1)):
    if nums1[n] in nums2:
        el=nums2.index(nums1[n])
        res.append(nums2.pop(el))
        
print(res)