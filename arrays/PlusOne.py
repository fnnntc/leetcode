digits=[8,9,9,9]
x=0
for d in range(len(digits)-1,-1,-1):
    if digits[d]<9:
        digits[d]+=1
        x=0
    elif digits[d]==9:
        digits[d]=0
        x=1
    if x==0:
        return(digits)
if x==1:
    return([1]+digits)