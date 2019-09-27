#!/usr/bin/python3

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
basket2 = set(['apple', 'orange', 'apple', 'pear', 'orange', 'banana'])

assert basket == basket2
assert 'orange' in basket
assert not 'crabgrass' in basket

#set operations
a = set('abracadabra')
b = set('alacazam')

assert (a - b) == {'r', 'd', 'b'} #letters in A but not in B (Difference)
assert (a | b) == {'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'} #letters in A or B (Union)
assert (a & b) == {'a', 'c'}  #letters in A and  B (Intersection)
assert (a ^ b) == {'r', 'd', 'b', 'm', 'z', 'l'}  #disjoint sets of letters in A B but not both (Mut-Ex)
