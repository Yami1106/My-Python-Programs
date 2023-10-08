S1=input("Enter first string")
S2=input("Enter second string")
str1=S1.lower()
str2=S2.lower()
dict1={}
dict2={}
for i in str1:
    if i not in dict1 :
        dict1[i]=0
        dict1[i]+=1
for j in str2 :
    if j not in dict2 :
        dict2[j]=0
        dict2[j]+=1
if dict1==dict2 :
    print("The entered strings are anagrams")
else :
    print("The entered strings are not anagrams")

