#formatter is a variable


formatter = "%r %r %r %r"
print (formatter %("one", "two", "three", "four"))
print (formatter %(True, False, False, True))
print (formatter %(formatter, formatter, formatter, formatter))
print (formatter %(
    "I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So i said goodnight."
	))
    
#python3

formatter = "{} {} {} {}"

print(formatter.format(1,2,3,4))
print(formatter.format("one","two","three","four"))
print(formatter.format(True,False,False,True))
print(formatter.format(formatter,formatter,formatter,formatter))
print(formatter.format("Try your", "Own text here", "Maybe a poem", "Or a song about fear"))