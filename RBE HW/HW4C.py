import math
import sys

print(sys.version)

x = float(input('What is the diameter of the wheel base (in cm)? '))
y = float(input("What is the diameter of the wheels (in cm)? "))


rotationDistance = 2*math.pi*((x/100)/2)
velocity = rotationDistance/2
angularRate = velocity/((y/100)/2)

print("The angular rate needed is " + str(angularRate) + " radians per second")