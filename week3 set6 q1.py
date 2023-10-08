class bird:
    def __init__(self,name,age):
        self.name=name
        self.age=age

blu=bird("Blu",10)
print("{} is a bird".format(blu.name))
woo=bird("Woo",15)
print("{} is also a bird".format(woo.name))
print("{} is {} years old".format(blu.name,blu.age))
print("{} is {} years old".format(woo.name,woo.age))