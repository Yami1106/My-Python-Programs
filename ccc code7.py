n=int(input("Enter nmber"))
for i in range(1,n):
    if(n>1):
        if(n%i==0):
            print("Not prime")
            break
        else:
            print("Is prime")
            break