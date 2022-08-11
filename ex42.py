## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass
 
 ## has-a relationship bw dog and animal
class Dog(Animal):
 
     def _init_(self,name):
        ##
        self.name = name

## has-a relationship bw cat and animal
class Cat(Animal):

    def _init_(self,name):
        ##
        self.name = name
         
## is-a relationship bw person and object
class Person(object):

    def _init_ (self, name):
        ## seff is-a name
        self.name = name
        
        ##Person has-a pet of some kind
        self.pet = None

##?? Employee is a person
class Employee (Person):

    def _init_(self, name, salary):
    ##
        super(Employee,self)._init_(name)
    ## Employee has-a salary
        self.salary = salary
        
## Fish is-a object
class Fish(object):
    pass

## Salmon is Fish
class Salmon(Fish):
    pass
    
    
##Halibut is-a fish
class Halibut(Fish):
    pass
    
## rover is-a Dog
rover = Dog()

# satan is a cat
satan = Cat()
