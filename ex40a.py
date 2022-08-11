# There is a problem in this file to run on line 20 attribution error, try to solve it.

mystuff = {'apple': "I AM APPLES!"}
print(mystuff['apple'])

#this goes in mystuff.py module and that is:
# I can use the module mystuff with import and then access the apple function:
def apple():
    print("I AM APPLES!")
    
    
import mystuff
mystuff.apple()

def apple():
    print("I AM APPLES!")
    
#this is just a varialbe
tangerine = "Living reflection of a dream"


#I can access the same way
print(mystuff.tangerine)

mystuff['apple'] #get apple from dict
mystuff.apple() # get apple from the module
mystuff.tangerine #same thing, it's just a variable

#classes are like modules
#if I were to create a class just like the mystuff module, I'd do something like this:

class MyStuff(Object)

    def_init_(self):
        self.tangerine = "And now a thousand years between"
        
    def apple(self):
        print("I AM CLASSY APPLES!")
        
#Objects are like Imports
#You instantiate(create) a class by calling the class like it's a function, like this:

thing = MyStuff()
thing.apple()
print(thing.tangerine)

#Getting Things from Things

#dict style
mystuff['apples']

#module style
mystuff.apples()
print(mystuff.tangerine)

#class style
thing = Mystuff()
thing.apples()
print(thing.tangerine)


