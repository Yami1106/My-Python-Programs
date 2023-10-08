from threading import *
l=Lock()
l.acquire()
print("lock acquired")
l.release()
print("lock released")