#this defines a new function(required parameters):
def cheese_and_crackers(cheese_count, boxes_of_crackers):
#What the function actually does. Formatters references argv parameters.
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"


print "We can just give the function numbers directly:"
#calling the function (give parameters, in any way.)
cheese_and_crackers(20, 30)


print "OR, we can use variables from our script:"
#this is just setting the variables to be used as parameters
amount_of_cheese = 10
amount_of_crackers = 50

#actually calling of the function (variables as parameters)
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too:"
#calling function (math, math)
cheese_and_crackers(10+20, 5+6)

print "And we can combine the two, variables and math:"
#both being used here
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
