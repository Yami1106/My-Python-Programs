class Example:
    def __init__(self):
        self.__private_data_member = 900

    def __private_method(self):
        print("This is a private method.")

    def public_method(self):
        print(f"The value of the private data member is: {self.__private_data_member}")

obj = Example()
obj.public_method()

try:
    obj.__private_data_member = 1000
except AttributeError as e:
    print("AttributeError: " + str(e))

try:
    obj.__private_method()
except AttributeError as e:
    print("AttributeError: " + str(e))
