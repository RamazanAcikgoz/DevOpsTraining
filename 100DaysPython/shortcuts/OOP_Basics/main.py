import carClass
import Tire


tire = Tire('P', 205, 55, 15)
tires = [tire, tire, tire]


auris = carClass('4-cylinder', tires=tires)

print(auris.description())