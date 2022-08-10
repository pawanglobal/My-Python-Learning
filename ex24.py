print ("Let's practice everything.")
print ("You\'d need ot know\'bout escapes with \\ that do \n newlines and \t tabs.")

poem = """
\tThe lovely world
with logic so firmly planted c
cannot discern \n the needs of love
nor comprehend passion from intuition
and comprehend passion fromm intuition
and requires an explanation
\n\t\twhere there is none.
"""
print ("_ _ _ _  _ _ _ _ __ _ __ _ _")
print (poem)
print ("_ _ _ _ __ _ _ _ _ _ _ __  _")

five = 10 - 2 + 3 - 6
print ("This should be five:%s" % five)

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans/100
    crates = jars/100
    return jelly_beans, jars, crates
    
    
    
start_point = 10000
beans,jars,crates = secret_formula(start_point)

print ("With a starting point of: %d" % start_point)
print ("We\'d have %d beans, %d jars, and %d crates." %(beans, jars, crates))

start_point = start_point / 10

print ("We can also do that this way:")
print ("We\d have %d beans, %d jars, and %d crates." %secret_formula(start_point))

#python3
print(f"This should be five: {five}")

#remeber that this is another way to format a string
print("With a starting point of: {}".format(start_point))
#it's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point/10

print ("We can also do that this way:")
formula = secret_formula(start_point)
#this is an easy way to apply a list to a format string
print("We'd have{} beans, {} jars, and {} crates.".format(*formula))


