import time
import threading
def calc_square(numbers):
    for n in numbers:
        time.sleep(0.5)
        print("square"+str(n*n))
def calc_cube(numbers):
    for n in numbers:
        time.sleep(0.5)
        print("cube"+str(n*n*n))
if __name__=="__main__":
    t=time.time()
    arr=[2,3,8,9]
    t1=threading.Thread(target=calc_square,args=(arr,))
    t2=threading.Thread(target=calc_cube,args=(arr,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("time taken ",time.time()-t)
