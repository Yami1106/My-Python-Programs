l=[]
for i in range(3):
    temp=[]
    for i in range(3):
        r=int(input())
        temp.append(r)
    l.append(temp)
for i in range(3):
    for j in range(3):
        print(end="")
    print(l[i])
