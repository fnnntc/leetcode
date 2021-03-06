nums = [4,3,2,7,8,2,3,1]
#nums=[1,1]
l=len(nums)
for i in range(l):
    x=abs(nums[i])
    nums[x-1]=-1*abs(nums[x-1])
    qwe =[i+1 for i in range(l) if nums[i]>0]
print(qwe)



'''
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]


Solution using Extra Space

Use a set (hash-map) and add all the numbers in this set. The set consists of all unique values within nums.
Iterate from [1 to N] and add to result list if i is not in the marked set.
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        marked = set(nums)
        return [i for i in range(1, len(nums)+1) if i not in marked]
Solution without using Extra Space

Can we avoid the set and somehow mark the input array which tells us what numbers are seen and what are not? We have additional information that the numbers are positive and numbers lie between 1 and N.
Approach 1: Iterate the array and mark the position implied by every element as negative. Then in the second iteration, we simply need to report the positive numbers.
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            x = abs(nums[i])
            nums[x-1] = -1*abs(nums[x-1])
        return [i+1 for i in range(len(nums)) if nums[i]>0]
Approach 2: Iterate the array and add N to the existing number at the position implied by every element. This means that positions implied by the numbers present in the array will be strictly more than N (smallest number is 1 and 1+N > N). Therefore. in the second iteration, we simply need to report the numbers less than equal to N to return the missing numbers..
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        N = len(nums)
        for i in range(len(nums)):
            nums[(nums[i]%N)-1] += N
        return [i+1 for i in range(len(nums)) if nums[i]<=N]