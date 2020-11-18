A=[5 ,5 ,4 ,5 ,5 ,5 ,4 ,5 ,6]
#A=[5, 4, 3 ,2 ,1 ,2 ,3 ,4 ,5 ,6]
#A=[9,7,5,3]
#A=[10 ,7 ,4 ,6 ,8 ,10 ,11]

T=int(input())
for t in range(T):
    A=[]
    l=int(input())
    for _ in input().split():
        A.append(int(_))
    if len(A)<2:
        print("Case #" + str(t + 1) + ": " + str(0))
    else:
        #print (A)
        cnt=0
        dist=[]
        res=0
            
        for i in range(1,len(A)):
            dist.append(A[i]-A[i-1])

        #print(dist)

        for d in range(len(dist)):
            if dist[d]==dist[d-1]:
                cnt+=1
            else:
                cnt=1
            if cnt>res:
                res=cnt
        print("Case #" + str(t + 1) + ": " + str(res+1))
