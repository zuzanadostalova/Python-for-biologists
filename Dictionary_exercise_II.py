# 21. Write a Python program to create and display all combinations of letters, selecting 
# each letter from a different key in a dictionary. 
dictionary = {'1':['a','b'], '2':['c','d']}
l = list(dictionary.items()) # [('1', ['a', 'b']), ('2', ['c', 'd'])]
print(l)

l1 = l[0][1]
l2 = l[1][1]
print(l1)
print(l2)

# Expected Output: 
# ac
# ad
# bc
# bd
x = l1[0:1]
y = l2[0:1]

# for key in l1:

from random import seed, randrange

seed(42)

def indexed_combination(seq, n):
    result = []
    for u in seq:
        if n & 1:
            result.append(u)
        n >>= 1
        if not n:
            break
    return result

print('Testing indexed_combination')
seq = ('1', ['a', 'b']), ('2', ['c', 'd'])
for i in range(1 << len(seq)):
    print(i, ''.join(indexed_combination(seq, i)))
print()

def random_combination(seq):
    n = randrange(1 << len(seq))
    return indexed_combination(seq, n)

print('Testing random_combination')
seq = 'abcdefghij'
for i in range(20):
    print(i, random_combination(seq))


# print(l1[0], l2[1])
# print(l1[0], l2[0])
# print(l1[1], l2[1])
# print(l1[1], l2[0])

# for key, value in dictionary.items():
#     if value in dictionary.values():
#         print(l[0][1]) # ['a', 'b']
#         # print(l[1][1]) ['c', 'd']