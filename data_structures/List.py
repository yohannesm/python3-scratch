#!/usr/bin/python3
import copy

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
assert fruits.count('apple') == 2

assert fruits.count('tangerine') == 0

assert fruits.index('banana') == 3

assert fruits.index('banana', 4) == 6

reversedFruits = copy.deepcopy(fruits)
reversedFruits.reverse()
print(reversedFruits)
print(fruits)

fruits.append('grape')

print(fruits)

fruits.sort()

print(fruits)

assert fruits.pop() == 'pear'

