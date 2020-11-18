"""Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.

Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2.  Elements that don't appear in arr2 should be placed at the end of arr1 in ascending order.

 

Example 1:

Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
Output: [2,2,2,1,4,3,3,9,6,7,19]"""

arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]
#order = {}
res=[]
#excluded=[]
l=len(arr2)
"""for i in range(l):
    order[i]=arr2[i]
"""
"""for j in order.values():
    for k in arr1:
        if k not in arr2:
            excluded.append(k)
        if k==j:
            res.append(j)"""
res=[]
l=len(arr2)

for i in range(l):
    cur=arr2[i]
    x=arr1.count(cur)
    for j in range(x):
        res.append(arr1.pop(arr1.index(cur)))

arr1.sort()
print(res+arr1)