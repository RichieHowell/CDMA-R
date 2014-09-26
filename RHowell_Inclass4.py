#Inclass4 Part 2

"""What does the code below do? Run the code in iPython.
For each line of code, add an explanation
through a comment."""

#PART I

#prints I will not count my chickens:
print "I will now count my chickens:"
#prints Hens 30, 30 because that is 25 + 30 /6
print "Hens", 25 + 30 / 6
#prints Roosters 97, 97 because that is the value of 100- 25 * 3 % 4
print "Roosters", 100 - 25 * 3 % 4
#prints now i will count the eggs:
print "Now I will count the eggs:"
#prints 7 because that is the value of 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6
print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6
#prints Is it true that 3 + 2 < 5 - 7
print "Is it true that 3 + 2 < 5 - 7?"
#prints false bcause 5 is greater than -2
print 3 + 2 < 5 - 7
#prints what is 3 + 2 ? 5 because 3 + 2 is 5
print "What is 3 + 2?", 3 + 2
#prints what is 5 - 7? -2 because 5 - 7 is -2
print "What is 5 - 7?", 5 - 7
#prints oh, that's why it's false
print "Oh, that's why it's False."
#prints how about some more.
print "How about some more."
#prints is it greater? true because 5 is greater than -2
print "Is it greater?", 5 > -2
#prints is it greater or equal? true because 5 is greater than or equal to -2
print "Is it greater or equal?", 5 >= -2
#prints is it less or equal? false because 5 is not less than or equal to -2
print "Is it less or equal?", 5 <= -2
#PART 

#sets the string variable days to the days of the week
days = "Mon Tue Wed Thu Fri Sat Sun"
#sets the months to the months of the year
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"
#prints the days seperated by spaces like they are int he string
print "Here are the days: ", days
#prints each month on its own line because they are seperated by the new line character
print "Here are the months: ", months

#PART III

#sets an list to the numbers between 1 and 5 inclusive
the_count = [1, 2, 3, 4, 5]
#sets a fruit list with fruits
fruits = ['apples', 'oranges', 'pears', 'apricots']
#sets a change list with numbers and strings
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#will print each number in the count list
for number in the_count:
    print "This is count %d" % number

#will print each string in the fruit list
for fruit in fruits:
    print "A fruit of type: %s" % fruit

# Use %r format when you don't know
#if the elements are strings or integers
#will print each element in the change list to give a human readable idea how how much change they have
for i in change:
    print "I got %r" % i

# we can also build lists, first start with an empty one
#initializes the elements list
elements = []

# then use the range function to do 0 to 5 counts
#uses a for loop to make i the numbers between 0 and 5
for i in range(0, 6):
    print "Adding %d to the list." % i
    # append is a function that lists understand
	#adds the numbers between 0 and 5 into the elements list
    elements.append(i)


#prints the numbers from 0 to 5 because that is what elements contains
for i in elements:
    print "Element was: %d" % i

#PART II

#Create comments where marked with # to explain the code below

#creates a states list with 5 states' full names as the index matched with their abrreviations  as the data
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

#creates a cities list with the abbreviates of states as the index matched with a large city from the state as the data
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

#creates 2 new elements in the cities list with the abbreviations of 2 states at the indexes and a big city found in that state as the data
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

#prints 10 dashes then says a big city of new york and a big city of oregan from the cities list
print '-' * 10
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

#prints 10 dashes then tells us the michigan and florida abbreviations from the states list
print '-' * 10
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

#prints 10 dashes then gives us a big city from michigan and florida by passing the data from the states list as the index of the city list
print '-' * 10
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

#prints 10 dahes then prints all the data with their indexes in the states list
print '-' * 10
for state, abbrev in states.items():
    print "%s is abbreviated %s" % (state, abbrev)

#prints 10 dahes then prints all the data with their indexes in the cities list
print '-' * 10
for abbrev, city in cities.items():
    print "%s has the city %s" % (abbrev, city)

#prints 10 dahes then prints all the data in both the lists by printing the index of the state list, then the data of the state list, then the data of the cities list using the data from the states list as an index
print '-' * 10
for state, abbrev in states.items():
    print "%s state is abbreviated %s and has city %s" % (
        state, abbrev, cities[abbrev])
