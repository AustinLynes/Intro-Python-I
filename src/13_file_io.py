"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE

# open up the file stream
with open("src/foo.txt", "r") as f:
    # get the text we are working with
    foo_txt = f.read()
    # print the text we are looking at
    print(foo_txt)

f.closed
# end of file read

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE

with open("src/bar.txt", "w") as b:
    b.write("something is better than nothing. \n")
    b.write('the answer is, 42. \n')
    b.write('beauty comes in many forms. and sometimes the evilest of wemon have the prettiest faces \n')

b.closed

with open("src/bar.txt", "r") as b_r:
    bar_txt = b_r.read()
    print(bar_txt)

b_r.closed