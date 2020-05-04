"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE

# find the length of the sys.argv property.
count = len(sys.argv)
# loop through the length
for i in range(count):
    print(f'{sys.argv[i]} \n')

# Print out the OS platform you're using:
# YOUR CODE HERE

os = sys.platform
print(f'{os}')
# Print out the version of Python you're using:
# YOUR CODE HERE

py_version = sys.version[0]
print(f'{py_version}')

import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html
# Print the current process ID
# YOUR CODE HERE
print(f'{os.getpgid(0)}')

# Print the current working directory (cwd):
# YOUR CODE HERE
print(f'{os.getcwd()}')
# Print out your machine's login name
# YOUR CODE HERE
print(f'{os.getlogin()}') # vagrant
import getpass
print(f'{getpass.getuser()}') # still vagrant... oh yeah... vagrant is a VE {virtual enviorment... so UBUNTU is what this is ran in..  aka linux.. makes sense}