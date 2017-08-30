#line 1-3: uses argv to get a filename.
from sys import argv

#line asking for argument variable. Script=__.py filename=whatever file you want
#to open. MAKE SURE FILE IS IN SAME DIRECTORY AS SCRIPT.
script, filename = argv

#NEW COMMAND: JUST THE FILE attached to variable "txt"
txt = open(filename)

#Printing a friendly line
print "Here's your file, %r:" % filename
#Printing the file-- variable(attached to file).read() --no parameters
print txt.read()

#Print another friendly line
print "Type the filmname again:"
#">" asks for data -- data gets assigned to variable "file_again"
file_again = raw_input("> ")

#OPEN = ATTACHED -- so this line only attaches the file to the variable
txt_again = open(file_again)

#Print line - .read() displays variable.
print txt_again.read()
