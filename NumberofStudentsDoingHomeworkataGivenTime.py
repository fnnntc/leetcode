class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        l=len(startTime)
        cnt=0
        for i in range(l):
            if startTime[i]<=queryTime<=endTime[i]:
                cnt+=1
        return(cnt)