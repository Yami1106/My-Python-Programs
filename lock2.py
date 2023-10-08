from threading import *
import time 
l=Lock()
def wish(name,age):
    for i in range (3):
        l.acquire()
        print("Hi",name)
        time.sleep(0.1)
        print("Your age is",age)
        l.release()
t1=Thread(target=wish,args=("Sireesh",15))
t2=Thread (target=wish,args=("Nithya",20))
t1.start()
t2.start()
