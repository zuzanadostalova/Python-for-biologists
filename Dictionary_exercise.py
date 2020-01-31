# # 1. Write a Python script to sort (ascending and descending) a dictionary by value. 

# # Solution I:
# d = {"bert":9,"emil":1,"celia":4,"abby":7,"dan":3,"fin":2,"gwyn":8}
# l = list(d.items())
# print(l)

# l.sort()
# print(l)
# # l.sort(reverse=True)
# # print(l)

# dict = dict(l)
# print("Dictionary", dict)
# # Output: Dictionary {'abby': 7, 'bert': 9, 'celia': 4, 'dan': 3, 'emil': 1, 'fin': 2, 'gwyn': 8}

# # Solution II:
# import operator
# d = {1:2, 3:5, 4:1, 6:3, 7:4}
# sorted_a = sorted(d.items(), key=operator.itemgetter(1))
# print(sorted_a) # Output: [(4, 1), (1, 2), (6, 3), (7, 4), (3, 5)]

# sorted_d = sorted(d.items(), key=operator.itemgetter(1), reverse=True)
# print(sorted_d) # Output: [(3, 5), (7, 4), (6, 3), (1, 2), (4, 1)]
# print(dict(sorted_d)) # Output: {3: 5, 7: 4, 6: 3, 1: 2, 4: 1}

# # 2. Write a Python script to add a key to a dictionary.

# #  Solution I:
# sample_dict = {0: 10, 1: 20}
# expect_result = {0: 10, 1: 20, 2: 30}

# sample_list = list(sample_dict.items())
# print(sample_list) # Output: [(0, 10), (1, 20)]

# new_key = [2, 30]
# sample_list.append(new_key)
# print(dict(sample_list)) # Output: {0: 10, 1: 20, 2: 30}

# #  Solution II:
# d = {0: 10, 1: 20}
# d.update({2: 30})
# print(d)  # Output: {0: 10, 1: 20, 2: 30}

# 3. Write a Python script to concatenate following dictionaries to create a new one.
dic1={1:10,2:20} 
dic2={3:30,4:40} 
dic3={5:50,6:60}
# # Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# Solution I:
list_1 = list(dic1.items())
list_2 = list(dic2.items())
list_3 = list(dic3.items())
list_all = list_1 + list_2 + list_3
print(dict(list_all)) # Output: {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# Solution II:
list_al = dict(list(dic1.items()) + list(dic2.items()) + list(dic3.items()))
print(list_al) # Output: {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# Solution III.:
dic4 = {}
for d in (dic1,dic2,dic3): # define d as the content of the three dict
    dict4 = dic4.update(d) # update the empty dict4 with the d content
    print(dict4) # Output: {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# 4. Write a Python script to check whether a given key already exists in a dictionary.
if 1 in dic1:
    print("It is there!")

for key in (dic4.items()):
    choice = input("Type in number of your choice: ")
    if choice in (dic4.items()):
        print("It is there!")
    else:
        print("No luck :(.")