s="(()())(())"

o=[]
ends=[]
l=len(s)
res=""

for i in range(l):
    if s[i]=="(":
        o.append(s[i])
        if len(o)==1:
            ends.append(i)
        else:
            res=res+(s[i])
    else:
        o.pop()
        if len(o)==0:
            ends.append(i)
        else:
            res=res+(s[i])


"""for j in range(l):
    if j not in ends:
        res=res+(s[j])"""
print(res)





"""A valid parentheses string is either empty (""), "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.  For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.

A valid parentheses string S is primitive if it is nonempty, and there does not exist a way to split it into S = A+B, with A and B nonempty valid parentheses strings.

Given a valid parentheses string S, consider its primitive decomposition: S = P_1 + P_2 + ... + P_k, where P_i are primitive valid parentheses strings.

Return S after removing the outermost parentheses of every primitive string in the primitive decomposition of S.

 

Example 1:

Input: "(()())(())"
Output: "()()()"
Explanation: 
The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
After removing outer parentheses of each part, this is "()()" + "()" = "()()()"."""
