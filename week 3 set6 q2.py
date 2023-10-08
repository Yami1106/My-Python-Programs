class B:
    def __init__(self):
        self.name = "Class B"
    def print_name(self):
        print(self.name)

class B1(B):
    def __init__(self):
        super().__init__()
        self.name = "Class B1"
    def print_name(self):
        print(self.name)

class B2(B):
    def __init__(self):
        super().__init__()
        self.name = "Class B2"
    def print_name(self):
        print(self.name)

class D(B1, B2):
    def __init__(self):
        super().__init__()

d = D()
d.print_name()
