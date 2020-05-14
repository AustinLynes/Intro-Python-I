"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string 
method, and by using f-strings.
"""

x = 10
y = 2.24552
z = "I like pandas!"

print('Using the printf operator (%), print the following feeding in the values of x'),
print("%s \n" % x)

print('y, and z')
print('%s and %s \n' % (y, z))

print("x is 10, y is 2.25, z is \"I like pandas!\"")
print("x is %s, y is %s, z is %s \n" % (x, y, z))

# Use the 'format' string method to print the same thing
print("x is 10, y is 2.25, z is \"I like pandas!\" -- format string --")

print("x is {x}, y is {y}, z is {z}  \n".format(x=x, y=y, z=z))

# Finally, print the same thing using an f-string
print("x is 10, y is 2.25, z is \"I like pandas!\" -- f-string --")
print(f"x is {x}, y is {y}, z is {z}  \n")