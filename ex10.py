tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm slit\non a line."
backlash_cat = "I'm\\a\\cat."
fat_cat = """
I'll do a list:
\t* cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""
print (tabby_cat)
print (persian_cat)
print (backlash_cat)
print (fat_cat)

# tiny piece of fun code 

while True:
     for i in ["/","-","|","\\","|"]:
        print ("%s\r" %i,) #to stop it Ctrl+c