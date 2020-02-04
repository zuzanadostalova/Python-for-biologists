# # 21. Write a Python program to create and display all combinations of letters, selecting 
# # each letter from a different key in a dictionary. 

# # Sol. I:
# dictionary = {'1':['a','b'], '2':['c','d']}
# l = list(dictionary.items()) # [('1', ['a', 'b']), ('2', ['c', 'd'])]
# print(l)

# # from random import seed, randrange

# # seed(42)

# # def indexed_combination(seq, n):
# #     result = []
# #     for u in seq:
# #         if n & 1:
# #             result.append(u)
# #         n >>= 1
# #         if not n:
# #             break
# #     return result

# # print('Testing indexed_combination')
# # seq = "abcd"
# # for i in range(2 << len(seq)):
# #     print(i, ''.join(indexed_combination(seq, i)))
# # print(l)

# # def random_combination(seq):
# #     n = randrange(2 << len(seq))
# #     return indexed_combination(seq, n)

# # print('Testing random_combination')
# # seq = 'abcdefghij'
# # for i in range(20):
# #     print(i, random_combination(seq))

# # Sol. II:
# import itertools      
# d ={'1':['a','b'], '2':['c','d']}
# for combo in itertools.product(*[d[k] for k in sorted(d.keys())]):
#     print(''.join(combo))

# # --------------------------------------------
# # Training
# l1 = l[0][1]
# l2 = l[1][1]
# print(l1)
# print(l2)

# # Expected Output: 
# # ac
# # ad
# # bc
# # bd
# x = l1[0:1]
# y = l2[0:1]

# # for key in l1:
# # print(l1[0], l2[1])
# # print(l1[0], l2[0])
# # print(l1[1], l2[1])
# # print(l1[1], l2[0])

# # for key, value in dictionary.items():
# #     if value in dictionary.values():
# #         print(l[0][1]) # ['a', 'b']
# #         # print(l[1][1]) ['c', 'd']

# # 22. Write a Python program to find the highest 3 values in a dictionary.
# from heapq import nlargest
# my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}  
# three_largest = nlargest(3, my_dict, key=my_dict.get)
# print(three_largest) 

# 23. Write a Python program to combine values in python list of dictionaries.
# Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
# Expected Output: Counter({'item1': 1150, 'item2': 300})
from collections import Counter
lst = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
# dict1 = list_all[0]
# print(dict1)
# amount = dict1["item"]
# print(amount)
# list2 = list_all[1]
# print(list2)
# list3 = list_all[2]
# print(list3)
# list_a = Counter({'item': 'item1', 'amount': 400})
# list_b = Counter({'item': 'item2', 'amount': 300})
# list_c = Counter({'item': 'item1', 'amount': 750})
# final = Counter(list_a) + Counter(list_b) + Counter(list_c) 
# print(final)

# final = ()
# for item in list_all:
#     amount = Counter({"amount"})

# if int in list_all:
#     print(int)
#     amount = Counter({int})
#     print(amount)

# dct_unpack = [x.items() for x in lst]
# print(dct_unpack)
# # Output: [dict_items([('item', 'item1'), ('amount', 400)]), dict_items([('item', 'item2'), 
# # ('amount', 300)]), dict_items([('item', 'item1'), ('amount', 750)])]

# list_a = dct_unpack[0]
# print(dct_unpack[1:])
# # dict_items([('item', 'item1'), ('amount', 400)])
# list_b = dct_unpack[1]
# # dict_items([('item', 'item2'), ('amount', 300)]) 
# list_c = dct_unpack[2]
# # dict_items([('item', 'item1'), ('amount', 750)])

# for key, value in dct_unpack.items():
#     print(key, 'is the key for the value', value)

from collections import Counter
item_list = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]

result = Counter()
for d in item_list:
    result[d["item"]] += d["amount"]
print(result)