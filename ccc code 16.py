st='naman'
st1=''
st2=''
for i in range(0,len(st)):
    st1+=st[i]
    st2+=st[len(st)-1-i]
if(st1==st2):
    print("palindrome")
else:
    print("not palindrome")

