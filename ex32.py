the_count = [1, 2, 3, 4, 5]
fruits = ['apple', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#this first kind of for-loop goes through a list
for number in the_count:
    print ("This is count %d" % number)
    
#same as above
for fruit in fruits:
    print ("A fuit of type: %s" %fruit)
 
#also we can go through mixed lists too
#notice we have to use % since we don't know what's in items
for i in change:
    print("I got %r" %i)
    
#also we can go through mixed lists too
#notice we have to use %r since we don't know what's in it
for i in change:
    print("I got %r" %i)

# we can also build lists, firs start with an empty one
elements = []

#then use the range function to do 0 to 5 counts
for i in range(0,6):
    print("Adding %d to the list." %i)
    #append is a fuction that lists understand
    elements.append(1)
    
#now we can print them out too
for i in elements:
    print("Element was: %d" %i)
    

#python3

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#this first kind of for-loop goes through a lish

for number in the_count:
    print(f"This is count{number}")

#same as above
for fruit in fruits:
    print(f"A fruit of type: {fruit}")
 
#also we can go through mixed lists too
#notice we have to use {} since we don't know what's in it

for i in change:
    print(f"I got{i}")
    
#we can also build lists, first start with an empty one
elements = []

#then use the range function to do 0 to 5 counts
for i in range(0,6):
    print(f"Adding {i} to the list.")
    #append is a function that lists understand
    elements.append(i)
    
#now we can print them out too
for i in elements:
    print(f"Elements was:(i)")
    

    