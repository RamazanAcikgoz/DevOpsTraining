class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")

class Fish(Animal): # We are inherit from Animal
    def __init__(self):
        super().__init__() # In order to get everything what have animal we should use 'super' keyword with  __init__()
        # It should be inside of init --> Animal is the super class of fish class

    def breathe(self):
        super().breathe()
        print("doing this underwater.")

    def swim(self):
        print("moving in water.")

nemo = Fish()
nemo.breathe()