# Swap two numbers using third variable
a = int(input('Enter the first number'))
b = int(input('Enter the second number'))
c = a
a = b
b = c
print('The first number is {} and the second number is {}.'.format(a,b))