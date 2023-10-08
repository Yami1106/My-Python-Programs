for i in range (0,5):
    id=int(input("Enter id"))
    name=input("Enter name")
    month=input("Enter month")
    units=int(input("Enter the units consumed"))
    if units<200:
        cost=units*1.2
    elif units>=200 and units<400:
        cost=(200*1.2)+((units-200)*1.5)
    elif units>=400 and units<600:
        cost= (200*1.2)+(200*1.5)+((units-400)*1.8)
    elif units>=600:
        cost= (200*1.2)+(200*1.5)+(200*1.8)+((units-600)*2)
    else :
        cost=100
    if cost>400:
        cost=cost+(cost*0.15)
        print("The bill for customer id {}, name {} for the month {} is {}".format(id,name,month,cost))