# Write a function is_even that will return true if the passed-in number is even.
# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE

# an even number is divisable by two (%2) 
# so if n % 2 == 0 then its divisable by 2

def even_odd(num):
    if num % 2  == 0: 
        print("Even!")
    else: 
        print("Odd")

even_odd(num)