x = "There are %d types of people." % 10
binary = "binary"
do_not = "do_not"
y = "Those who know %s and those who %s." %(binary, do_not)
print (x)
print (y)
print ("I said: %r." %x)
print ("I also said: '%s'." %y)
hilarious = False
joke_evaluatuion = "Isn't that joke so funny?!" 
print ("%s %s" %(joke_evaluatuion,hilarious))
w = "This is the left side of..."
e = "a string with a right side."
print (w+e)

#python3

types_of_people = 10
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said: {x}")
print(f"I alos said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print(w+e)
