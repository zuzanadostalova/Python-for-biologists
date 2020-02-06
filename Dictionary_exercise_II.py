# # # 21. Write a Python program to create and display all combinations of letters, selecting 
# # # each letter from a different key in a dictionary. 

# # # Sol. I:
# # dictionary = {'1':['a','b'], '2':['c','d']}
# # l = list(dictionary.items()) # [('1', ['a', 'b']), ('2', ['c', 'd'])]
# # print(l)

# # # from random import seed, randrange

# # # seed(42)

# # # def indexed_combination(seq, n):
# # #     result = []
# # #     for u in seq:
# # #         if n & 1:
# # #             result.append(u)
# # #         n >>= 1
# # #         if not n:
# # #             break
# # #     return result

# # # print('Testing indexed_combination')
# # # seq = "abcd"
# # # for i in range(2 << len(seq)):
# # #     print(i, ''.join(indexed_combination(seq, i)))
# # # print(l)

# # # def random_combination(seq):
# # #     n = randrange(2 << len(seq))
# # #     return indexed_combination(seq, n)

# # # print('Testing random_combination')
# # # seq = 'abcdefghij'
# # # for i in range(20):
# # #     print(i, random_combination(seq))

# # # Sol. II:
# # import itertools      
# # d ={'1':['a','b'], '2':['c','d']}
# # for combo in itertools.product(*[d[k] for k in sorted(d.keys())]):
# #     print(''.join(combo))

# # # --------------------------------------------
# # # Training
# # l1 = l[0][1]
# # l2 = l[1][1]
# # print(l1)
# # print(l2)

# # # Expected Output: 
# # # ac
# # # ad
# # # bc
# # # bd
# # x = l1[0:1]
# # y = l2[0:1]

# # # for key in l1:
# # # print(l1[0], l2[1])
# # # print(l1[0], l2[0])
# # # print(l1[1], l2[1])
# # # print(l1[1], l2[0])

# # # for key, value in dictionary.items():
# # #     if value in dictionary.values():
# # #         print(l[0][1]) # ['a', 'b']
# # #         # print(l[1][1]) ['c', 'd']

# # # 22. Write a Python program to find the highest 3 values in a dictionary.
# # from heapq import nlargest
# # my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}  
# # three_largest = nlargest(3, my_dict, key=my_dict.get)
# # print(three_largest) 

# # 23. Write a Python program to combine values in python list of dictionaries.
# # Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
# # Expected Output: Counter({'item1': 1150, 'item2': 300})
# from collections import Counter
# lst = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
# # dict1 = list_all[0]
# # print(dict1)
# # amount = dict1["item"]
# # print(amount)
# # list2 = list_all[1]
# # print(list2)
# # list3 = list_all[2]
# # print(list3)
# # list_a = Counter({'item': 'item1', 'amount': 400})
# # list_b = Counter({'item': 'item2', 'amount': 300})
# # list_c = Counter({'item': 'item1', 'amount': 750})
# # final = Counter(list_a) + Counter(list_b) + Counter(list_c) 
# # print(final)

# # final = ()
# # for item in list_all:
# #     amount = Counter({"amount"})

# # if int in list_all:
# #     print(int)
# #     amount = Counter({int})
# #     print(amount)

# # dct_unpack = [x.items() for x in lst]
# # print(dct_unpack)
# # # Output: [dict_items([('item', 'item1'), ('amount', 400)]), dict_items([('item', 'item2'), 
# # # ('amount', 300)]), dict_items([('item', 'item1'), ('amount', 750)])]

# # list_a = dct_unpack[0]
# # print(dct_unpack[1:])
# # # dict_items([('item', 'item1'), ('amount', 400)])
# # list_b = dct_unpack[1]
# # # dict_items([('item', 'item2'), ('amount', 300)]) 
# # list_c = dct_unpack[2]
# # # dict_items([('item', 'item1'), ('amount', 750)])

# # for key, value in dct_unpack.items():
# #     print(key, 'is the key for the value', value)

# from collections import Counter
# item_list = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]

# result = Counter()
# for d in item_list:
#     result[d["item"]] += d["amount"]
# print(result)

# 24. Write a Python program to create a dictionary from a string. 
# Note: Track the count of the letters from the string.
# Sample string : 'w3resource'
# Expected output: {'3': 1, 's': 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}

# string = "w3resource"
# dictionary = {}
# for character in string:
#     # print(character) - printing the character - 3, s...
#     # print(string.count(character)) - just all the counts each on a new line

#     dictionary[character] = string.count(character) # opening the dictionary and assign.
#     # to the key "character" value which is the "count of the particular character in the
#     # string
# print(dictionary)

# ??? 25. Write a Python program to print a dictionary in table format. 
# my_dict = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
# for row in zip(*([key] + (value) for key, value in sorted(my_dict.items()))):
#     print(row)

# ??? 26. Write a Python program to count the values associated with key in a dictionary.
# list_ = [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success': False, 'name': 'Rabi'}, 
# {'id': 3, 'success': True, 'name': 'Alex'}]
# import itertools  
# d = dict(itertools.zip_longest(*[iter(list_)] * 2, fillvalue=""))
# print(d)
# dict1 = list_[0]
# print(dict1)
# dict2 = list_[1]
# dict3 = list_[2]

# sum( x == True for x in dict_.values())
# You're trying to use a dict as a key to another dict or in a set. That does not work because
# the keys have to be hashable. As a general rule, only immutable objects (strings, integers, 
# floats, frozensets, tuples of immutables) are hashable (though exceptions are possible).
# print(sum)
# # Counter({1: 1, 3: 1, 2: 0})

# 27. Write a Python program to convert a list into a nested dictionary of keys.
l = ["id1", "a", "A", "id2", "b", "B", "id3", "c", "C", "id4", "d", "D", "id5", "e", "E"]
# it = iter(l)     
# # print(dict(zip(it, it)))
# dict_ = dict(zip(*[iter(l)]*2))
# print(dict_) #... simple dictionary
# # {'id1': 'a', 1: 'id2', 'b': 2, 'id3': 'c', 3: 'id4', 'd': 4, 'id5': 'e'}

# # Sol. I:
# dict_ = {}
# for path in l:
#     current_level = dict_
#     for part in path:
#         if part not in current_level:
#             current_level[part] = {}
#         current_level = current_level[part]
# print(dict_)

# # Sol.II:
# dict_ = current = {}
# for string in l:
#     current[string] = {}
#     current = current[string]
# print(dict_)
# # {'D': {'id5': {'e': {'E': {}}}}}}}}}}}}}}}}

# # Sol.III:
# def build_tree(l):
#     if l:
#         return {l[0]: build_tree(l[1:])}
#     return {}

# print(build_tree(l))
# # {'D': {'id5': {'e': {'E': {}}}}}}}}}}}}}}}}

# # 28. Write a Python program to sort a list alphabetically in a dictionary.
# # Sol.I:
# l = ["a", "c", "h", "t", "r", "l", "o", "q"]
# l.sort() # do not assign it to anything
# print(l)

# # Sol. II:
# d = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}
# for i, j in d.items(): 
#     sorted_dict ={i:sorted(j)} 
#     print(sorted_dict)
# # {'n1': [1, 2, 3]}
# # {'n2': [1, 2, 5]}
# # {'n3': [2, 3, 4]}

# ['a', 'c', 'h', 'l', 'o', 'q', 'r', 't']
# dictionary = dict.fromkeys(l, 1)
# print(dictionary)
# {'a': 1, 'c': 1, 'h': 1, 'l': 1, 'o': 1, 'q': 1, 'r': 1, 't': 1}

# # Sol.III:
# d = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}
# sorted_dict = {x: sorted(y) for x, y in d.items()}
# print(sorted_dict)
# # {'n1': [1, 2, 3], 'n2': [1, 2, 5], 'n3': [2, 3, 4]}

# # 29. Write a Python program to remove spaces from dictionary keys.
# # Sol. I:
# d = {'n  1': [2, 3, 1], 'n  2': [5, 1, 2], 'n   3': [3, 2, 4]}
# d = {k.replace(" ",""): v for k,v in d.items()}
# print(d)
# # {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}

# d_new = d = {}
# for key in inside_d:
#     d[key] = {}
#     d = d[key]
# print(d_new)

# F - j, s

# # ?? Sol. II:
# d = {'n  1': [2, 3, 1], 'n  2': [5, 1, 2], 'n   3': [3, 2, 4]}
# d = {x.translate({32: None}): y for x, y in d.items()}
# print(d)
# # The translate() method takes the translation table to replace/translate 
# # characters in the given string as per the mapping table.
# # {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}

# # 30. Write a Python program to get the top three items in a shop. 
# # Sample data: {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
# # Sol. I:
# from heapq import nlargest
# data = {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
# # for key, value in data.items():
#     # print(key, value)
# three_largest = nlargest(3, data, key=data.get)
# print(three_largest)
# # ['item4', 'item1', 'item3']

# from operator import itemgetter
# for key, value in nlargest(3, data.items(), key=itemgetter(1)):
#     print(key, value)
# # item4 55
# # # item1 45.5
# # # item3 41.3

# # Sol. II:
# from operator import itemgetter
# data = {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
# for key, value in nlargest(3, data.items(), key=itemgetter(1)):
#     print(key,value)
# # item4 55
# # item1 45.5
# # item3 41.3

# 31. Write a Python program to get the key, value and item in a dictionary. 
dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# Sol. I:
# print("key","value","count")
# for key, value in dict_num.items():
#     count = key
#     print(key, " ", value, "   ", count)

# # Enumerate() - count of iterations
# # Sol. II:
# print("key","value","count")
# for count, (key, value) in enumerate(dict_num.items(), 1):
#     print(key, " ", value, "   ", count)
# # Sol.I + Sol.II output:
# # key value count
# # 1   10     1
# # 2   20     2
# # 3   30     3
# # 4   40     4
# # 5   50     5
# # 6   60     6

# # 32. Write a Python program to print a dictionary line by line.
# students = {'Aex':{'class':'V',
#         'rolld_id':2},
#         'Puja':{'class':'V',
#         'roll_id':3}}
# # for line in students:
# #     print(line)
# for key in students:
#     print (key)
#     for value in students[key]:
#         print (value,':',students[key][value])
#     # replace - string

# # 33. Write a Python program to check if multiple keys exist in a dictionary.
# # Sol.I:
# students = {'Aex':{'class':'V',
#         'rolld_id':2},
#         'Puja':{'class':'V',
#         'roll_id':3}}
# print(len(students)) # number of keys 2
# print(students.keys() >= {"Aex", "Puja"}) # True
# print(students.keys() >= {"Aex", "roll_id"}) # False

# # Sol.II:
# student = {
#   'name': 'Alex',
#   'class': 'V',
#   'roll_id': '2'
# }

# # print(len(student)) # number of keys 3
# print(student.keys() >= {"class", "name"}) # True
# print(student.keys() >= {"class", "Alex"}) # False
# print(student.keys() >= {"class", "roll_id"}) # True

# # 34. Write a Python program to count number of items in a dictionary value that is a list.
# dict =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}

# # Sol.I:
# print(len(dict.keys()))
# # 2 - just keys

# print(len(set(open("Dict1.txt").read().split())))
# # 6 - all unique words in the file

# # Sol.II:
# ctr = sum(map(len, dict.values()))
# print(ctr)
# # 5 - why the difference?

# # 35. Write a Python program to sort Counter by value
# from collections import Counter
# dicti = Counter({'Math':81, 'Physics':83, 'Chemistry':87})
# print(dicti)
# # Counter({'Chemistry': 87, 'Physics': 83, 'Math': 81})
# print(dicti.most_common()) # the same function indeed

# 36. Write a Python program to create a dictionary from two lists without losing duplicate values
# # Sample lists: ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII'], [1, 2, 2, 3]
# list_ = ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII']
# id_list = [1, 2, 2, 3]
# # d = {key: value for (key, value) in list_}
# # print(d)

# from collections import defaultdict
# temp = defaultdict(set)
# for c, i in zip(list_, id_list):
#     temp[c].add(i)
# print(temp)
# defaultdict(<class 'set'>, {'Class-V': {1}, 'Class-VI': {2}, 'Class-VII': {2}, 'Class-VIII': {3}})


# 37. Write a Python program to replace dictionary values with their sum.
# dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# ctr = sum(dict_num.values())
# print(ctr)

# student_details= [
#   {'id' : 1, 'subject' : 'math', 'V' : 70, 'VI' : 82},
#   {'id' : 2, 'subject' : 'math', 'V' : 73, 'VI' : 74},
#   {'id' : 3, 'subject' : 'math', 'V' : 75, 'VI' : 86}
# ]

# def sum_v1_v2_average(student_details):
#     for d in student_details:
#         v1 = d.pop('V')
#         v2 = d.pop('VI')
#         d['V+VI'] = (v1 + v2)/2
#     return student_details
# print(sum_v1_v2_average(student_details))

# # [{'subject': 'math', 'id': 1, 'V+VI': 76.0}, {'subject': 'math', 'id': 2, 'V+VI': 73.5}, {'subject': 'math', 
# # 'id': 3, 'V+VI': 80.5}]

# 38. Write a Python program to match key values in two dictionaries.
dict_ = {'key1': 1, 'key2': 3, 'key3': 2}
dict_1 = {'key1': 1, 'key2': 2}

# for key in dict_:
#     # value = dict_1[key]
#     if key in dict_1:
#         if dict_[key] == dict_1[key]:
#             print("These keys are the same: " + key)
#         else:
#             print("These keys differ: " + key)
# These keys are the same: key1
# These keys differ: key2

# for (key, value) in set(dict_.items()) & set(dict_1.items()):
#     print('%s: %s is present in both dict_ and dict_1' % (key, value))

# 39. Write a Python program to store a given dictionary in a json file. 
# Original dictionary:
# {'students': [{'firstName': 'Nikki', 'lastName': 'Roysden'}, {'firstName': 'Mervin', 'lastName': 'Friedland'}, {'firstName': 'Aron ', 'lastName': 'Wilkins'}], 'teachers': [{'firstName': 'Amberly', 'lastName': 'Calico'}, {'firstName': 'Regine', 'lastName': 'Agtarap'}]}
# <class 'dict'>     

dicti = {'students': [{'firstName': 'Nikki', 'lastName': 'Roysden'}, {'firstName': 'Mervin', 
'lastName': 'Friedland'}, {'firstName': 'Aron ', 'lastName': 'Wilkins'}], 'teachers': 
[{'firstName': 'Amberly', 'lastName': 'Calico'}, {'firstName': 'Regine', 'lastName': 'Agtarap'}]}

# # Sol.I:
# import json
# with open('result.json', 'w') as fp:
#     json.dump(dicti, fp)   

# with open('result.json') as f:
#   data = json.load(f)
# print(data)
# # {'students': [{'firstName': 'Nikki', 'lastName': 'Roysden'}, {'firstName': 'Mervin', 
# # 'lastName': 'Friedland'}, {'firstName': 'Aron ', 'lastName': 'Wilkins'}], 'teachers': 
# # [{'firstName': 'Amberly', 'lastName': 'Calico'}, {'firstName': 'Regine', 'lastName': 'Agtarap'}]}
# # print(type(data))

# # Sol.II:
# d = {"students":[{"firstName": "Nikki", "lastName": "Roysden"},
#                {"firstName": "Mervin", "lastName": "Friedland"},
#                {"firstName": "Aron ", "lastName": "Wilkins"}],
# "teachers":[{"firstName": "Amberly", "lastName": "Calico"},
#          {"firstName": "Regine", "lastName": "Agtarap"}]}
# print("Original dictionary:")
# print(d)

# import json
 
# with open("dictionary", "w") as f:
#    json.dump(d, f, indent = 4, sort_keys = True)
 
# print("\nJson file to dictionary:")
# with open('dictionary') as f:
#  data = json.load(f)
# print(data)

# # 40. Write a Python program to create a dictionary of keys x, y, and z where each key has as 
# # value a list from 11-20, 21-30, and 31-40 respectively. Access the fifth value of each key from 
# # the dictionary.
{'x': [11, 12, 13, 14, 15, 16, 17, 18, 19],
'y': [21, 22, 23, 24, 25, 26, 27, 28, 29],
'z': [31, 32, 33, 34, 35, 36, 37, 38, 39]}

from pprint import pprint
dict_nums = dict(x=list(range(11, 20)), y=list(range(21, 30)), z=list(range(31, 40)))
pprint(dict_nums)
print(dict_nums["x"][4])
print(dict_nums["y"][4])
print(dict_nums["z"][4])
for k,v in dict_nums.items():
   print(k, "has value", v)