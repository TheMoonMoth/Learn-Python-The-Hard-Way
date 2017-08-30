#THIS SECTION IS JUST SETTING UP VARIABLES

#x is a variable. the string contains a formatter- a variable for
x = "There are %d types of people." %10
#two variables set as strings
binary = "binary"
do_not = "don't"
#a variable set to a string. %s references two variables defined in line 4 and 5
y = "Those who know %s and those who %s." %(binary, do_not)

#ACTUAL PRINTING OF LINES
#x will show -- There are 10 types of people.
print x
#y will show -- Those who know binary, and those who don't.
print y

#print line - Formatter within string is referencing variable x.
#%r will show 'singles quotes' around reference string
print "I said: %r." %x
#print line - formatter within string is referencing variable y.
#%s will NOT show 'single quotes' around reference string.
#unless the 'single quotes' are within the main string.
print "I also said: '%s'" %y

#Variable set as a value.
hilarious = False
#variable set as a string
joke_evaluation = "Isn't that joke so funny?! %r"

#print line -- variable references string, '% hilarious' is formatter
#-- referenced by the string.
print joke_evaluation % hilarious

#setting variables
w = "this is the left side of..."
e = "a string with a right side."

#printing variables as if it were math.
print w + e
