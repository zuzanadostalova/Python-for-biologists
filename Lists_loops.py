# # Lists and loops
# # item in a list = element

# # To get an element, write the index
# apes = ["Homo sapiens", "Pan  troglodytes", "Gorilla gorilla"]
# conserved_sites = [24, 56, 132]
# print(apes[0])
# first_site = conserved_sites[2]

# # # If we want to know the index and we know element; use index()
# apes = ["Homo sapiens", "Pan  trglodytes", "Gorilla gorilla"]
# chimp_index = apes.index("Pan troglodytes")

# # # chimp index now 1

# last_ape = apes[-1]

# ranks = ["kingdom", "phylum", "class", "order", "family"]
# lower_ranks = ranks[2:5]
# # # lower ranks are class, order, and family
# # # we can treat a string as a list

# # Working with list elements
# # to add another element into an existing list -> .append()
# apes = ["Homo sapiens", "Pan  troglodytes", "Gorilla gorilla"]
# print(apes)
# apes.append("Pan paniscus")
# print(apes)

# # .append() changes the variable -> e.g. from 3 elements to 4
# # len()
# apes = ["Homo sapiens", "Pan  troglodytes", "Gorilla gorilla"]
# print("There are " + str(len(apes)) + " apes")
# apes.append("Pan paniscus")
# print("Now there are " + str(len(apes)) + " apes")

# # we can concatenate lists with +
# apes = ["Homo sapiens", "Pan  troglodytes", "Gorilla gorilla"]
# monkeys = ["Papio ursinus", "Macaca mulatta"]
# primates = apes + monkeys

# print(str(len(apes)) + " apes")
# print(str(len(monkeys)) + " monkeys")
# print(str(len(primates)) + " primates")

# # add an element to an existing list - takes a list as an argument
# # reverse and sort - change the order in the list 

# ranks = ["kingdom", "phylum", "class", "order", "family"]
# print("At the start: " + str(ranks))

# ranks.reverse()
# print("After reversing: " + str(ranks))

# ranks.sort()
# print("After sorting: " + str(ranks))

# # Writing a loop - instead of printing them separately
# for ape in apes:
#     print(ape + " is an ape")

# variable used in a loop does not have an value, it is automatically set to each
# element of the list, different each time around the loop
# indented lines - body of the loop, otherwise block of code
# we cannot change the list while in the body of the loop

# apes = ["Homo sapiens", "Pan  troglodytes", "Gorilla gorilla"]

# for ape in apes:
#     name_length = len(ape)
#     first_letter = ape[0]
#     print(ape + " is an ape. Its name starts with " + first_letter)
#     print("It's name has " + str(name_length) + " letters.")

# two print statements - everytime two lines of output
# if only two print statements - easier changes
# adding elements to the loop - we do not need to change the loop

# # Indentation errors
# apes = ["Homo sapiens", "Pan  troglodytes", "Gorilla gorilla"]

# for ape in apes:
#     name_length = len(ape)
#    first_letter = ape[0]
#     print(ape + " is an ape. Its name starts with " + first_letter)

# # because the lines of the code do not match up
# # only space or tab for indentation -> tab emulation

# # Using a string as a list
# # string in the position of a list -  each character in the list as a separate element

# name = "python"
# for character in name:
#     print("One character is: " + character)
# # repeating a set of information for each element of the list = iteration
# # iteration over a list or a string

# # Splitting a string to make a list
# # split() takes a single argument called delimiter and splits the string 
# # where it sees the delimeter producing a list
# names = "melanogaster,simulans,yakuba,ananasse"
# species = name.split(",")
# print(str(species))

# # this created list can be iterated over using a loop

# # Iterating over lines in a file
# # both string and file can be treated as list and iterate over
# # but in string each character becomes an individual element whereas in a file
# # each line becomes an individual element

# # iterating over file object not contents
# file = open("some_input.txt")
# for line in file:

# # iterating over file contents
# file = open("some_input.txt")

# # print length of each line
# for line in file:
#     print("The length is " + str(len(line)))

# # print the first character of each line
# for line in file:
#     print("The first character is " + line[0]) # this line never gets executed
# # because file objects are exhaustible - it reads all the lines in the first for loop

# # solution:
# # I. reopen the file each time
# # II. read the lines of the file into a list, iterate over list, .readlines() returns 
# # a list of all the lines in the file

# # store a list of lines in the file
# file = open("some_input.txt")
# all_lines = file.readlines()

# # print the lengths
# for line in all_lines:
#     print("The length is " + str(len(line)))

# # print the first characters
# for line in all_lines:
#     print("The first character is " + line[0])

# # Loops with ranges
# # iterate over a list of numbers

protein = "vlspadktnv"
print(protein[0:3]) # substring notation, without loop repetitive
# Output: "vls"

# solution - range() - generates lists of numbers (Python2), range object (Python3)
# its behaviour depends on the number of the arguments

# single argument - count up from 0 to that number
for number in range(6):
    print(number)
# Output: from 0 to 5

# two numbers
for number in range(3, 7):
    print(number)
# Output: from 3 to 8

# three numbers
for number in range(2, 14, 4):
    print(number)
# Output: 2, 6, 10

# lists - many elements in a single variable
# loops - let us process these elements one by one