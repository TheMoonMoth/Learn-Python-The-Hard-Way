#This imports the arugment variable (still unclear)
from sys import argv

#Variables that must be defined in the command line.
script, user_name = argv
#prompt variable = "Whatever I want."
prompt = 'Answer here>'

#print line- % references user_name, which was defined by the argv
print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."

print "Do you like me, %s?" % user_name
#answer for this input gets assigned to the 'likes' variable
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "what kind of computer do you have?"
computer = raw_input(prompt)

#block text refencing user defined variables.
print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)
