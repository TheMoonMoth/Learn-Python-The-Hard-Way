#variable set to a string of formatters
formatter = "%s %s %s %s"

#print line- "format variable" % then references the (1,2,3,4)
print formatter % (1, 2, 3, 4)
#print line- quotes will be visible for %r but not for %s
print formatter % ("one", "two", "three", "four")
#print line- "format variable" % referencing the ()
print formatter % (True, False, False, True)

#this is the line with the formatter inside the formatter
print formatter % (formatter, formatter, formatter, formatter)

print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)
