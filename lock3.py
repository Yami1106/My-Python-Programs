from threading import *
import time
l=RLock()     #for recursive programs
def factorial(n):
    l.acquire()
    if n==0:
        result=1
    else:
        result=n*factorial(n-1)
    l.release()
    return result
def results(n):
    print("the Factorial of",n,"is:",factorial(n))
t1=Thread(target=results,args=(5,))
t2=Thread(target=results,args=(9,))
t1.start()
t2.start()

