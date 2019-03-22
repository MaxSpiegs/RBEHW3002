import math
import sys

print(sys.version)

x = float(input('What is the diameter of the wheel base? '))
y = float(input("What is the diameter of the wheels? "))


rotationDistance = 2*math.pi*(x/2)
velocity = rotationDistance/2
angularRate = velocity/(y/2)

print("The angular rate needed is " + str(angularRate) + " radians per second")