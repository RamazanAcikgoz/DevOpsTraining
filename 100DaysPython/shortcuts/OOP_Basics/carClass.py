class Car:
    # For documentation we can use docstring """ /
    """
    Docstring describing the class
    Car models a car w/ tires and an engine
    """
    def __init__(self, engine, tires):
        self.engine = engine
        self.tires = tires
        
        # pass # it means we wont implement it right now

# __init__ this is the thing that happens when we create a new instance (constructor)
# it calls dunder method (double under methods)

# Classes are the blueprint for creating individual version of a thing

    def description(self):
        # We need to have a self argument for methods which in class
        # function and method are the same. Methods attached to objects
        print(f"A car with an {self.engine} engine, and {self.tires} tires")