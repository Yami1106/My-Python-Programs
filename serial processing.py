import time
def calc_square(numbers):
    for n in numbers:
        time.sleep(0.0000001)
        print("square"+str(n*n))
def calc_cube(numbers):
    for n in numbers:
        time.sleep(0.0000001)
        print("cube"+str(n*n*n))

arr=[2,3,8,9]
t=time.time()
calc_square(arr)
calc_cube(arr)
print("done in",time.time()-t)