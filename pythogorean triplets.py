print("Enter the first edge")
a=input()
a=int(a)
print("Eneter the second edge")
b=input()
b=int(b)
print("Enter the third edge")
c=input()
c=int(c)
if a*a+b*b==c*c or b*b+c*c==a*a or a*a+c*c==b*b :
    print("Pythogorean triplets")
else :
    print("Not Pythogorean triplets")