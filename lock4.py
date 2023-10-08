from threading import *
import time 
s=Semaphore(5)

def wish(name,age):
    for i in range(3):
        s.acquire()
        print("Hi",name)
        time.sleep(0.0001)
    s.release()
t1=Thread(target=wish,args=("Sireesh",15))
t2=Thread(target=wish,args=("Nithya",20))
t3=Thread(target=wish, args=("Shiva",16))
t4=Thread(target=wish, args=("Ajay",25))
t1.start()
t2.start()
t3.start()
t4.start()


