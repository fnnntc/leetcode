nums1 = [4,1,2]
nums2 = [1,3,4,2]
#nums1 = [2,4]
#nums2 = [1,2,3,4]
"""res=[]
for n in nums1:
    l=len(res)
    x = nums2.index(n)
    for m in nums2[x+1:]:
        if m > n:
            res.append(m)
            break
    if len(res)==l:
        res.append(-1)

print(res)"""

stack, m = [], {}
for num in nums2:
    while stack and stack[-1] < num:
        m[stack.pop()] = num
    stack.append(num)
ret = []
for num in nums1:
    ret.append(m.get(num, -1))
print (ret)