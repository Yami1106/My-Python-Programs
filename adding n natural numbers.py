def add_n(n):
    if n==1:
        return 1
    else:
        return n+add_n(n-1)

k=int(input("Enter a number"))
print("The sum of numbers upto k is:")
print(add_n(k))