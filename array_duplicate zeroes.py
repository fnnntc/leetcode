class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        l=len(arr)
        i=0
        while i<l:
            print("i={}".format(i))
            if arr[i]==0:
                for j in range(l-1,i,-1):
                    arr[j]=arr[j-1]
                i+=1
            i+=1

