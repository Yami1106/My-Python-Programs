for i in range(0,5):
    id=int(input("Enter your id"))
    name=input("Enter your name")
    unit1=int(input("Enter the units consumed in first month"))
    unit2=int(input("Enter the units consumed in second month"))
    unit3=int(input("Enter the units consumed in third month"))
    avg = (unit1+unit2+unit3)/3
    if avg<=unit3 :
        unit4=unit3
        print("Domestic")
    else :
        print("commercialized")

