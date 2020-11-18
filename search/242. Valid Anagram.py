s = "rat"
t = "cat"
ls,lt=len(s),len(t)
if ls!=lt:
    print(False)
    #return False
sd,td={},{}
for i in range(len(s)):
    sd[s[i]]=s.count(s[i])
    td[t[i]]=t.count(t[i])
print(sd==td)