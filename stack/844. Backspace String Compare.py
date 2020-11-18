import functools
S = "hd#dp#czsp#####"
T = "hd#dp#czsp#######"


stacks=[]
for S in [S,T]:
    i=0
    stack=[]
    for c in S:
        if c=="#":
            if stack:
                stack.pop()
        else:
            stack.append(c)
    stacks.append(stack)
print(functools.reduce(lambda  x,y: x==y, stacks))

"""
stacks=[]
for S in [S,T]:
    i=0
    stack=[]
    for c in S:
        # сделать добавление только если не звездочка
        stack.append(c)
    while i < len(stack):
        if stack[i]=="#":
            stack.pop(i)
            if i>0:
                stack.pop(i-1)
                i-=1
        else:
            i+=1
    stacks.append(stack)

print(functools.reduce(lambda  x,y: x==y, stacks))
"""