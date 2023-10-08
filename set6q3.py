for i in range (0,5):
    id=int(input("Enter customer id"))
    name= input("Enter your name")
    unit1= int(input("Enter the units consumed for first month"))
    unit2=int(input("Enter the units consumed for second month"))
    unit3=int(input("Enter the units consumed for third month"))
    avg=float((unit1+unit2+unit3)/3)
    if avg<=unit3 :
        unit4=unit3
        print("predicted number of units are {}".format(unit4))
    else :
        print("unpredictable")