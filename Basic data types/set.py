#python set

#unordered collection of items
#unique values
#items of set should be immutable but set it self is mutable
#we can add or remove items from set


set1 = {1, 2,3}
print(set1, type(set1))

#set1 = {1, ['mandar', 'handsome'], 3} we can not add list in set
print(set1, type(set1))

set1 = {1, tuple(['mandar', 'handsome']), 3}
print(set1, type(set1))

set1 = set([1, 2, 3])
print(set1, type(set1))

set1 = {} #empty dict
print(set1, type(set1))

set1 = set()
print(set1, type(set1))

ls1 = ['m', 1, 'mandar', 0.0 ]
set1 = {1, 2, 3}

set1.add('mandar')
print(set1, type(set1))

set1.update(ls1)
print(set1, type(set1))

#set1.add(ls1) can not add mutable using add method
#print(set1, type(set1))

set1.update([4,5], {1,6,8})
print(set1, type(set1))

set1.discard(9) # will not raise error though item is not present in set
print(set1, type(set1))

#set1.remove(9) # will raise KeyError if item is not present in set
print(set1, type(set1))

set1.discard(4)
set1.remove(5)
print(set1, type(set1))

set2 = {1,2,3,4}
set3 = {3,4,5,6,7}

#union
print('set2 union set3', set2 | set3, set2.union(set3))
print('set2 intersection set3', set2 & set3, set2.intersection(set3))
print('set3 difference set3', set2 - set3, set2.difference(set3), set3 - set2, set3.difference(set2))
print('set2 symmetric_difference set3', set2 ^ set3, set2.symmetric_difference(set3))

l1 = [1,2,3,4]
l2 = [3,4,5,6,7]

set2 = set()
set3 = set()
set2.update(l1)
set3.update(l2)
print(list(set2 & set3), list(set2 ^ set3))

l1 = [1,2,3,4]
l2 = [3,4,5,6,7]
#lc = [x for x in l1 for y in l2 if x == y]
lc = [x for x in l1 for y in l2 if x == y]
print(lc)

A = frozenset([1, 2, 3, 4])
B = frozenset([3, 4, 5, 6])
print(A ,B, A | B, A & B, A - B, A ^ B)

