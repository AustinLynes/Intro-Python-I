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
# loop through the length
print(f'sys : #1')
for i in range(len(sys.argv)):
    print(f'argv property {i}: {sys.argv[i]} \n')

# Print out the OS platform you're using:
# YOUR CODE HERE
print(f'sys : #2')
print(f'operating_system: {sys.platform} \n')
# Print out the version of Python you're using:
# YOUR CODE HERE
# for i in range(len(sys.version)):
#     print(f'{sys.version[i]} \n')
print(f'sys : #3')
print(f'python_version: {sys.version}  \n')
import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html
# Print the current process ID
# YOUR CODE HERE
print(f'os : #1')
print(f'current_process_id: {os.getpgid(0)} \n')

# Print the current working directory (cwd):
# YOUR CODE HERE
print(f'os : #2')
print(f'current_working_directory: {os.getcwd()}')
# Print out your machine's login name
# YOUR CODE HERE
print(f'os : #3')
print(f'login_username: {os.getlogin()}') # vagrant

## my idea behind this stretch was to see if because since i setup the vagrant client 
## and now an using the linux enviorment for programming so i was wondering if the method that 
## the docs mentioned would get my username.. and. 
print(' -- stretch --')
import getpass
print(f'login_username_with_getpass: {getpass.getuser()}') # still vagrant... oh yeah... vagrant is a VE {virtual enviorment... so UBUNTU is what this is ran in..  aka linux.. makes sense}