def add(a, b):
    print "Adding %d + %d" % (a, b)
    return a + b

def subtract(a, b):
    print "Subtracting %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "Multipying %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "Dividing %d / %d" % (a, b)
    return a / b


print "Let's do some math with just functions!"

age = add(30.00, 5.00)
height = subtract(78.00, 4.00)
weight = multiply(90.00, 2.00)
iq = divide(100.00, 2.00)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)


#a puzzle for the extra credit, type it anyway.
print "Here is a puzzle."

#nesting egg --last-f(variable, 4ction(variable 3rd function(2, f(1st, first))))
what = add(age, multiply(age, multiply(iq, divide(height, iq))))

print "That becomes: ", what, "can you do it by hand?"
