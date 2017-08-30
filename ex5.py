name = 'Kyle A. Weintraub'
age = 26 #not a lie
height = 12*6+3 #inches
weight = 161 #pounds
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." %name
print "He's %d inches tall." %height
print "He's %d pounds heavy." %weight
print "Actually that's not heavy enough."
print "He's got %s eyes and %s hair." %(eyes, hair)
print "His teeth are usually %s depending on the coffee." %teeth

#this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." %(
    age, height, weight, age + height + weight)
