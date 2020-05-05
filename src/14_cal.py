"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.

Note: the user should provide argument input (in the initial call to run the file) and not 
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to 
print out a calendar for April in 2015, but if you omit either the year or both values, 
it should use today’s date to get the month and year.

"""

from os import system, name
import sys
import calendar
from datetime import datetime

# check_num 
# takes _a number and _b number
# and checks to see if a > b
# if a > b then returns error 

def check_num(_a, _b):
  if _a > _b:
    print("error")


def main(*args):
  now = datetime.now()
  date = (str)(now)[:10]
  txt_cal = calendar.TextCalendar(6)
  # splitting above to create inp.. 
  # this creates a list we need to go inside the first index of the list 
  # and see if its currently is an empty string.. meaning the user just hit [ enter ]
  _month = date[5:7]
  _year = date[:4]

  if len(args[0]) == 3: 
    y = (int)(args[0][2])
    m = (int)(args[0][1])
    print(m > 0)
    if(m <= 12 and m > 0):
      _month = m 
    else: 
      print('Month Error, Month should be less than 12 and greater than 0')
      return
    if(y <= 5000 and y >= 1):
      _year = y
    else: 
      print('Year Error, Month should be no less than 1 and no greater than 5000')
      return
  elif len(args[0]) == 2:
    m = (int)(args[0][1])
    if(m <= 12 and m > 0):
      _month = m 
    else: 
       print('Month Error, Month should be less than 12 and greater than 0')
       return
  elif( len(args[0]) > 3):
    print('Too Many Arguments. expects maximum of { Month,  Year }')
    return 

  
  print(txt_cal.formatmonth(themonth=(int)(_month), theyear=(int)(_year)))

main(sys.argv)