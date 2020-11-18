strs=["flower", "flow","flight"]

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if strs:
            l=min([len(x) for x in strs])
        else:
            return("")
        word=strs[0]
        i,cnt=0,0

        while i<l:
            letter=word[i]
            for s in strs[1:]:
                if s[i]==letter:
                    cnt+=1
                else:
                    return(word[:i])
            i+=1

        return(word[:i])