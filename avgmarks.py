for x in range(5):
    n=input("Ente Name: ")
    a=int(input("Enter maks of Physics: ")) 
    b=int(input("Enter maks of Chemistry: "))
    c=int(input("Enter maks of Maths: "))
    s=a+b+c
    avg=s/3
    print("Sum = ",s,end="\n")
    print("Average = ",avg,end="\n")
    if(avg>50):
        print("Grade = Pass")
    else:
        print("Grade = Fail")
