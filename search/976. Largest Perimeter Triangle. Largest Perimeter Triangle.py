"""Given an array A of positive lengths, return the largest perimeter of a triangle with non-zero area, formed from 3 of these lengths.

If it is impossible to form any triangle of non-zero area, return 0.

 

Example 1:

Input: [2,1,2]
Output: 5
Example 2:

Input: [1,2,1]
Output: 0
Example 3:

Input: [3,2,3,4]
Output: 10
Example 4:

Input: [3,6,2,3]
Output: 8"""

def largestPerimeter(A):
    i,j=0,2
    l=len(A)
    vars=[]
    for i in range(l-2):
        for j in range(2,l):
            for k in range(i+1,j):
                if A[i]+A[j]>A[k] and A[k]+A[j]>A[i] and A[i]+A[k]>A[j]:
                    vars.append(A[i]+A[k]+A[j])
    return(max(vars))

A=[1,2,2,4,18,8]

print(largestPerimeter(A))