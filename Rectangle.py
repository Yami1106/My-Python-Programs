class Rectangle: #(Constructor)
    def __init__(self,width,height):
        self.width=width #<...attribute
        self.height=height
    def calculate_area(self):
        return self.width*self.height
r1=Rectangle(1,2) #<..object instance of the class
print(r1.calculate_area()) #<...call method of object
print(r1.width)
r1.width=5