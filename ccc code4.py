x=int(input("Enetr number"))
if(x%2==0):
    if(x%3==0):
        print("Number is divisible by both 2 and 3")
    else:
        print("Number is only divisible by 2")
elif(x%3==0):
        print("Number is only divisible by 3")
else:
     print("Number is not divisible by both 2 and 3")
    