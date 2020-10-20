#Author: Ethan Brydon
#Date: 14/09/2019
#Purpose: This program takes 3 side lengths as input and 
# uses them to calculate the area of a triangle.

import math

#Gathers input 
a = float(input("Enter side length a: "))
b = float(input("Enter side length b: "))
c = float(input("Enter side length c: "))

#Calculates S and side lengths and outputs statement
S = (a + b + c)/2
Area = (S*(S - a)*(S - b)*(S - c))**(1/2)
Area = round(Area, 4)
print("The area of a triangle with side lengths of "+str(a)+", "+str(b)+", "+str(c)+" is "+str(Area)+".")