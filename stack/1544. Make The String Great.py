s = "abBAcC"
st=[]
for c in s:
    st.append(c)

i=0
while i<len(st)-1:
    if st[i]!=st[i+1] and st[i].upper()==st[i+1].upper():
        st.pop(i)
        st.pop(i)
        i=0
    #elif st[i]!=st[i-1] and st[i].upper()==st[i-1].upper():
    #    st.pop(i-1)
    #    st.pop(i-1)
    else:
        i+=1
print("".join(st))
