def square(a):
    print "I will now square %d" % a
    return a * a

def add(a, b):
    print "Let's add those together."
    return a + b


print "How much is 10 squared?"
answer = square(10)
print answer

print "How much is 5 squared?"
answer2 = square(5)

print "Add %d and %d and we get?" % (answer, answer2)
total = add(answer, answer2)
print total
