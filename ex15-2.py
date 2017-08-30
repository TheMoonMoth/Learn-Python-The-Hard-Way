#line 1-3: uses argv to get a filename.
from sys import argv

#line asking for argument variable. Script=__.py filename=whatever file you want
#to open. MAKE SURE FILE IS IN SAME LOCATION AS SCRIPT.
script, filename = argv

#NEW COMMAND: JUST THE FILE attached to variable "txt"
txt = open(filename)

#Printing a friendly line
print "Here's your file, %r:" % filename
#Printing the file-- variable(attached to file).read() --no parameters
print txt.read()
