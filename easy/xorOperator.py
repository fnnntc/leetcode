class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums=[start+2*x for x in range(n)]
        res = reduce(ixor, nums) 
        return res