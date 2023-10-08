class Student:
    def __init__(self, name, age=12, classroom=7):
        self.name=name
        self.age=age
        self.classroom=classroom
    #DISPLAY student
    def show(self):
        print(self.name,self.age,self.classroom)
s1=Student('mike')
s1.show()
kelly=Student('Kelly',13)
kelly.show()