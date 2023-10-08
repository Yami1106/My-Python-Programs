import time
import multiprocessing
def calc_square(numbers):
    for n in numbers:
        print("square"+str(n*n))
def calc_cube(numbers):
    for n in numbers:
        print("cube"+str(n*n*n))
if __name__=="__main__":
    arr=[2,3,8,9]
    t1= multiprocessing.Process(target=calc_square,args=(arr,))
    t2= multiprocessing.Process(target=calc_cube,args=(arr,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("done")
    
