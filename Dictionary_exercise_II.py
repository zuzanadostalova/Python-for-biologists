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

# T - ch, l, a...F - j, s

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
count = []
