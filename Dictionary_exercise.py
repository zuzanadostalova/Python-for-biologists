# # # # 1. Write a Python script to sort (ascending and descending) a dictionary by value. 

# # # # Solution I:
# # # d = {"bert":9,"emil":1,"celia":4,"abby":7,"dan":3,"fin":2,"gwyn":8}
# # # l = list(d.items())
# # # print(l)

# # # l.sort()
# # # print(l)
# # # # l.sort(reverse=True)
# # # # print(l)

# # # dict = dict(l)
# # # print("Dictionary", dict)
# # # # Output: Dictionary {'abby': 7, 'bert': 9, 'celia': 4, 'dan': 3, 'emil': 1, 'fin': 2, 'gwyn': 8}

# # # # Solution II:
# # # import operator
# # # d = {1:2, 3:5, 4:1, 6:3, 7:4}
# # # sorted_a = sorted(d.items(), key=operator.itemgetter(1))
# # # print(sorted_a) # Output: [(4, 1), (1, 2), (6, 3), (7, 4), (3, 5)]

# # # sorted_d = sorted(d.items(), key=operator.itemgetter(1), reverse=True)
# # # print(sorted_d) # Output: [(3, 5), (7, 4), (6, 3), (1, 2), (4, 1)]
# # # print(dict(sorted_d)) # Output: {3: 5, 7: 4, 6: 3, 1: 2, 4: 1}

# # # # 2. Write a Python script to add a key to a dictionary.

# # # #  Solution I:
# # # sample_dict = {0: 10, 1: 20}
# # # expect_result = {0: 10, 1: 20, 2: 30}

# # # sample_list = list(sample_dict.items())
# # # print(sample_list) # Output: [(0, 10), (1, 20)]

# # # new_key = [2, 30]
# # # sample_list.append(new_key)
# # # print(dict(sample_list)) # Output: {0: 10, 1: 20, 2: 30}

# # # #  Solution II:
# # # d = {0: 10, 1: 20}
# # # d.update({2: 30})
# # # print(d)  # Output: {0: 10, 1: 20, 2: 30}

# # # 3. Write a Python script to concatenate following dictionaries to create a new one.
# # dic1={1:10,2:20} 
# # dic2={3:30,4:40} 
# # dic3={5:50,6:60}
# # # # Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# # # Solution I:
# # list_1 = list(dic1.items())
# # list_2 = list(dic2.items())
# # list_3 = list(dic3.items())
# # list_all = list_1 + list_2 + list_3
# # print(dict(list_all)) # Output: {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# # # Solution II:
# # list_al = dict(list(dic1.items()) + list(dic2.items()) + list(dic3.items()))
# # print(list_al) # Output: {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# # # Solution III.:
# # dic4 = {}
# # for d in (dic1,dic2,dic3): # define d as the content of the three dict
# #     dic4.update(d) # update the empty dict4 with the d content
# #     print(dic4) # Output: {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# # # 4. Write a Python script to check whether a given key already exists in a dictionary.

# # # Solution I:
# # # Not automatized
# # if 1 in dic4:
# #     print("It is there!")
# # else:
# #     print("No luck.")

# # # Solution II:
# # def if_number_present(x):
# #     if x in dic4:
# #         print("It is there!")
# #     else:
# #         print("No luck.")
# # if_number_present(7)
# # if_number_present(1)

# # for key in (dic1,dic2,dic3):
# #     choice = input("Type in number of your choice: ")
# #     if choice in (dic1,dic2,dic3):
# #         print("It is there!")
# #     else:
# #         print("No luck :(.")

# # # 5. Write a Python program to iterate over dictionaries using for loops.
# # d = {"bert":9,"emil":1,"celia":4,"abby":7,"dan":3,"fin":2,"gwyn":8}
# # for key in d:
# #     print(key.count("a"))
    
# # 6. Write a Python script to generate and print a dictionary that contains 
# # a number (between 1 and n) in the form (x, x*x). 
# # Sample Dictionary ( n = 5) : 
# # Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# # # print(dict in range(1,5))
# # # False?!

# # # ???
# # n = int(input("Pick up a number: ")) # e.g. 6
# # d = dict() # d member of dictionary

# # for x in range(1,n+1): # key = unknown number from the range 1 to the desired number + 1
# #     d[x] = x*x # value = square unknown number

# # print(d) # print dictionary

# # # 7. Write a Python script to print a dictionary where the keys are numbers between 1 and 15
# # # (both included) and the values are square of keys

# # # d = dict()

# # # for x in range(1,16):
# # #     d[x] = x*x
# # # print(d)
# # # # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81,
# # # #  10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}

# # # 8. Write a Python script to merge two Python dictionaries.

# # # Solution I:
# # d1 = {6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
# # d2 = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
# # l1 = list(d1.items())
# # l2 = list(d2.items())
# # l3 = l2 + l1
# # print(dict(l3))
# # # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}

# # # Solution II:
# # d1 = {6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
# # # d2 = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
# # # d = d1.copy()
# # # d.update(d2)
# # # print(d)
# # # # Output: {6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# # # # 9. Write a Python program to iterate over dictionaries using for loops. 
# # d1 = {"six": 36, "seven": 49, "eight": 64, "nine": 81, "ten": 100, "eleven": 121, "twelve": 144, 
# # "thirteen": 169, "fourteen": 196, "fifteen": 225}
# # for word_key, value in d1.items():
# #     print(word_key)

# # 10. Write a Python program to sum all the items in a dictionary.
# d1 = {"six": 4, "seven": 5}

# print(sum(d1.values()))
# # Output: 9

# # # 11. Write a Python program to multiply all the items in a dictionary. 
# my_dict = {'data1':100,'data2':-54,'data3':247}
# result=1
# for key in my_dict:    
#     result=result * my_dict[key]

# print(result)

# # 12. Write a Python program to remove a key from a dictionary.
# my_dict = {'data1':100,'data2':-54,'data3':247}
# del(my_dict["data1"])
# print(my_dict)

# # 13. Write a Python program to map two lists into a dictionary.
# list1 = ["Mary", "John", "Joseph", "Kate"]
# list2 = ["David", "Jack", "Joe", "Kim"]
# dictionary = dict(zip(list1, list2))
# print(dictionary) # {'Mary': 'David', 'John': 'Jack', 'Joseph': 'Joe', 'Kate': 'Kim'}

# for odd_no in range(1,20,5):
# Output: 1, 6, 11, 16
# for odd_no in range(1,20):
#     if(odd_no % 2 != 0):
#         print(odd_no)

# # 14. Write a Python program to sort a dictionary by key.
# list1 = [4, 0, 2, 1]
# list2 = ["David", "Jack", "Joe", "Kim"]

# # Sol. I: 
# list1.sort()
# dictionary = dict(zip(list1, list2))
# print(dictionary)

# # # Sol. II:
# # dictionary_ = {'Mary': "teacher", 'John': "pilot", 'Joseph': 'fisherman', 'Kate': 'miner'}
# # sorting even string
# dictionary_ = {0: 'David', 1: 'Jack', 2: 'Joe', 4: 'Kim'}
# # for key in sorted(dictionary_):
#     # print("%s: %s" % (key, dictionary_[key]))
# # for value does not work

# # 15. Write a Python program to get the maximum and minimum value in a dictionary. 
# # Sol. I:
# print(max(dictionary_))
# print(min(dictionary_))
# # Print: 4, 0

# my_dict = {'x':500, 'y':5874, 'z': 560}
# key_max = max(my_dict.keys(), key =(lambda k: my_dict[k]))
# key_min = min(my_dict.keys(), key =(lambda k: my_dict[k]))
# print(max(my_dict))
# print(min(my_dict))
# # Output: z, x - wrong

# print(my_dict[key_max])
# print(my_dict[key_min])
# Output: 5874, 500 - correct, because I am asking for a value from dictionary

# # 16. Write a Python program to get a dictionary from an object's fields.
# Example 1:
# class Colors(object): # be sure to write double underscore
#     def __init__(self):
#         self.x = 'red'
#         self.y = 'Yellow'
#         self.z = 'Green'

#     def do_nothing(self):
#         pass

# c = Colors()

# print(c.__dict__) # be sure to write double underscore
# Output: {'x': 'red', 'y': 'Yellow', 'z': 'Green'}
# -----------------------------------------------
# Example 2:
# class animals(object):
#     def __init__(self): 
#         self.x = "cat"
#         self.y = "dog"
#         self.z = "rabbit"

#     def do_nothing(self):
#         pass

# a = animals()
# print(a.__dict__)
# Output: {'x': 'cat', 'y': 'dog', 'z': 'rabbit'}
# -----------------------------------------------
# # Example 3:
# class days(object):

#     def __init__(self):
#         self.m = "Monday"
#         self.t = "Tuesday"
#         self.w = "Wednesday"
#     def do_nothing(self):
#         pass

# d = days()
# print(d.__dict__)
# Output: {'m': 'Monday', 't': 'Tuesday', 'w': 'Wednesday'}


# # 17. Write a Python program to remove duplicates from Dictionary.
# d = {"x": "Jen", 'y':"Dan", 'y':"Dan", 'z':"Benji"} # input 1
# # d = {"id1": {'x':["Jen"], 'y':["Dan"]}, "id2": {'y':["Dan"], 
# # 'z': ["Benji"]}, "id3": {'x':["Jen"], 'y':["Dan"]}} # input 2

# final = {}

# for key, value in d.items():
#     if value not in final.values():
#         final[key] = value
#     # if value in d.values():
#     #     d[key] = value
# print(final)
# Output I: {'x': 'Jen', 'y': 'Dan', 'z': 'Benji'}
# Output II: {'id1': {'x': ['Jen'], 'y': ['Dan']}, 'id2': {'y': ['Don'], 'z': ['Benji']}}

# the key is to print each value once, assigning value to the key only once
# omitting the whole id3 subdictionary


# ?
# l = list(d.items())
# [dict(t) for t in {tuple(d.items()) for d in l}]
# set(tuple(d.items()) for d in l)

# # 18. Write a Python program to check a dictionary is empty or not
# dictionary = {}

# if not bool(dictionary):
#     print("The dictionary is empty.")


# # 19. Write a Python program to combine two dictionary adding values for common keys. 
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# # Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})

# # l1 = list(d1.items())
# # d3 = {}

# # Sol. I:
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# for key in d1:
#     if key in d2:
#         d1[key] = d2[key] + d1[key]
#     else:
#         pass
# print(d1)
# # Output: {'a': 400, 'b': 400, 'c': 300} but "d" is missing

# # Sol. II:
# from collections import Counter
# d1 = Counter({'a': 100, 'b': 200, 'c':300})
# d2 = Counter({'a': 300, 'b': 200, 'd':400})
# d = Counter(d1) + Counter(d2)
# print(d)
# # Output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})

# Error trial
# for key, value in d1.items():
#     if "a" in d2.keys():
#         l1 = list(d1.items())
#         l2 = list(d2.items())
#         # l1.append(l2[0])
#         # add
#         l1.add(l2[0])

#     if "b" in d2.keys():
#         # l1.append(l2[1])
#         l1.add(l2[1])

#     if "c" in d2.keys():
#         # l1.append(l2[2])
#         l1.add(l2[2])
#     print(l1)

# 20. Write a Python program to print all unique values in a dictionary.
# Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}

# # Sol. I:
# def unique(list1):
#     unique_list = []

#     for x in list1:
#         if x not in unique_list:
#             unique_list.append(x)
#     for x in unique_list:
#         print(x)

# list1 = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, 
# {"V":"S009"},{"VIII":"S007"}] 
# print("The unique values from the list are: ")
# unique(list1) # without print otherwise it prints "None"
# The unique values from the list are:
# {'V': 'S001'}
# {'V': 'S002'}
# {'VI': 'S001'}
# {'VI': 'S005'}
# {'VII': 'S005'}
# {'V': 'S009'}
# {'VIII': 'S007'}

# Sol. II:
L = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, 
{"V":"S009"},{"VIII":"S007"}] 

u_value = set(val for dic in L for val in dic.values()) # ?
print("Unique values", u_value)

# Output: Unique values {'S009', 'S002', 'S007', 'S005', 'S001'}

