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

# Indentation errors
apes = ["Homo sapiens", "Pan  troglodytes", "Gorilla gorilla"]

for ape in apes:
    name_length = len(ape)
   first_letter = ape[0]
    print(ape + " is an ape. Its name starts with " + first_letter)

# because the lines of the code do not match up
# only space or tab for indentation -> tab emulation

# Using a string as a list
# string in the position of a list -  each character in the list as a separate element

name = "python"
for character in name:
    print("One character is: " + character)
# repeating a set of information for each element of the list = iteration
# iteration over a list or a string

# Splitting a string to make a list
# split() takes a single argument called delimiter and splits the string 
# where it sees the delimeter producing a list
names = "melanogaster,simulans,yakuba,ananasse"
species = name.split(",")
print(str(species))

# this created  list can be iterated over using a loop



