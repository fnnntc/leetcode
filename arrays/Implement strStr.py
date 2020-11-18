


def strStr(haystack, needle):
    h_l = len(haystack)
    n_l = len(needle)

    for i in range(h_l):
        if not needle:
            return -1
        if haystack[i]==needle[0] and len(haystack[i:]) >= n_l:
            isStr=True
            for j in range(n_l):
                if needle[j] != haystack[i+j]:
                    isStr=False
                    break
            if isStr:
                return(i)
    return(-1)

print(strStr("aaa","aaaa"))
assert (strStr("hello","1")== -1)
assert (strStr("hello","ll")== 2)
assert (strStr("hello","lle")== -1)
assert (strStr("hello","")== -1)
assert (strStr("","")== 0)