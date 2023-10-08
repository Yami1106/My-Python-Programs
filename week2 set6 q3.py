def bank(n,p):
    credentials={"Ramesh": "12345", "Seetha": "abcde", "Abhishek": "pqrst", "Ramya": "98765", "Priya": "xyzab"}
    if credentials.get(n) is None :
        print("Your details does not match with our records")
    
    else :
        print(("Dear {}, you are welcome to our bank".format(n)))
        
            
bank("Ramesh","12345")
bank("Abhsk","1245")



