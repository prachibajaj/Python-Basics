import math

a = float(input('Enter the first side of triangle:'))
b = float(input('Enter the second side of triangle:'))
c = float(input('Enter the third side of triangle:'))

s = (a+b+c)/2
#print(s)
 
a = s*(s-a)*(s-b)*(s-c)
area = math.sqrt(a)
print("The area of given triangle is {}".format(area))