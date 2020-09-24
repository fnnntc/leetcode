s = "(([{}])))}"

openers = "[", "{", "("
closers = "]", "}", ")"

res=[]
for c in s:
    if c in openers: 
        res.append(c)
    elif len(res)==0 or openers.index(res.pop()) != closers.index(c):
        print("False")
print("True")

