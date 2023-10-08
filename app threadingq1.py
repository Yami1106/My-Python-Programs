from threading  import *
import time 
def wish(name, age):
    for i in range(3):
        print("Hi",name)
        time.sleep(2)
        print("Your age is", age)
t1=Thread(target=wish,args=("Sireesh",15))
t2=Thread(target=wish,args=("Nithya",20))
t1.start()
t2.start()

