m=input("Enetr the month")
print("List of months: Janusry,Febuary,March,April,May,June,July,August,September,October,November,December")
if(m=='January'or'March'or'May'or'July'or'August'or'October'or'December'):
    print("31 days")
elif(m=='February'):
    print("28/29 days")
else:
    print("30 Days")