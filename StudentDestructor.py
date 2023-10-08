class Student:
    def __init__(self,name):
        print("Inside Constructor")
        self.name=name
        print("Object Initialized")
    def show(self):
        print("Hello,My name is",self.name)
    #dectructor
    def __del__(self):
        print("Inside Destructor")
        print("Object Destroyed")
s1=Student('Mike')
s1.show()
del s1 #delete object
