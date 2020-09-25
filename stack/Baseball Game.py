class Solution:
    def calPoints(self, ops: List[str]) -> int:
        res=[]
        for i in ops:
            if i == "C":
                res.pop()
            elif i == "D":
                x = res[-1]*2
                res.append(x)
            elif i == "+":
                x = res[-1] + res[-2]
                res.append(x)
            else:
                res.append(int(i))
        return(sum(res))