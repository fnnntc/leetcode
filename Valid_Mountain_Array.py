arr = [0,1,2,3,4,5,6,7,8,9]

l=len(A)
        cnt=0
        i,j=0,1
        isUp,isDown = False, False
        if l<3:
            return (False)
        if A[0]>A[1] or l<3:
            return (False)
        while j<l and A[i]<A[j]:
            if A[i]==A[j]:
                return (False)
            cnt+=1
            i+=1
            j+=1
            isUp = True
        while j<l and A[i]>A[j]:
            if A[i]==A[j]:
                return (False)
            cnt+=1
            i+=1
            j+=1
            isDown = True
        if cnt==l-1 and isUp and isDown:
            return (True)
        else:
            return (False)
