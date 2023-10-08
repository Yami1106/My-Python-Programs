class Parent:
    def __init__(self):
        print("Parent class constructor.")
        
    def parent_method(self):
        print("This is a method from the parent class.")

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child class constructor.")
        
    def child_method(self):
        print("This is a method from the child class.")

child = Child()
child.parent_method()
child.child_method()
