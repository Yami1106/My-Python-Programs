def genpass(name,birthdate):
    password=name[:4].lower()+birthdate[:4]
    print("Your password is :",password)

name=input("Enter your name: ")
date=input("Enter your date of birth(ddmmyyyy): ")
genpass(name,date)
