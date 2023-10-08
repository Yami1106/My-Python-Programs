class Flying:
    def fly(self):
        raise NotImplementedError("The fly method must be implemented by a subclass.")

class Parrot(Flying):
    def fly(self):
        print("Parrot can fly.")

class Penguin(Flying):
    def fly(self):
        print("Penguin cannot fly.")

def flying_test(bird):
    bird.fly()

parrot = Parrot()
penguin = Penguin()

flying_test(parrot)
flying_test(penguin)
