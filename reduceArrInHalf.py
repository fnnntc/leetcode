from collections import Counter
arr = [3,3,3,3,5,5,5,2,2,7]
#arr = [1,2,3,4,5,6,7,8,9,10]
'''l=len(arr)
h=l//2
cnt=0
i=0
s=set(arr)
lengths=[arr.count(x) for x in s]
lengths.sort(reverse=True)
while cnt<h:
    cnt+=lengths[i]
    i+=1
print(i)'''
l=len(arr)
h=l//2
cnt,i=0,0
test_list=Counter(arr)
res=test_list.most_common()
while cnt<h:
    print(cnt)
    cnt+=res[i][1]
    i+=1
print(i)
