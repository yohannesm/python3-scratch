#!/usr/bin/python3
from math import pi

squares = []
for x in range (10):
    squares.append(x**2)
assert squares == [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

squaresF1 = list(map(lambda x: x**2, range(10)))
assert squaresF1 == [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

squaresF2 = [x**2 for x in range(10)]
assert squaresF2 == [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

combs1 = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
assert combs1 == [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

vec = [-4, -2, 0, 2, 4]
vec_m2 = [x*2 for x in vec]
assert vec_m2 == [-8, -4, 0, 4, 8]

vec_filter2 = [x for x in vec if x >= 0]
assert vec_filter2 == [0, 2, 4]

vec_apply_abs = [abs(x) for x in vec]
assert vec_apply_abs == [4, 2, 0, 2, 4]

freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
weapons = [weapon.strip() for weapon in freshfruit]
print(weapons)

vec2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flatten_vec2 = [num for elem in vec2 for num in elem]
assert flatten_vec2 == [1, 2, 3, 4, 5, 6, 7, 8, 9]

complex_pi_formatting = [str(round(pi, i)) for i in range(1, 6)]
print(complex_pi_formatting)

name = ["Marcell", "Charles", "Lelouch", "Astra"]
roll_no = [4, 1, 3, 2]
marks = [90, 50, 60, 30]
#Make a set of Tuple3 using zip
mapped_set = set(zip(name, roll_no, marks))
print(mapped_set)
#Make a dict using zip
mapped_dict = dict(zip(name, marks))
print(mapped_dict)

print("comprehension finished")
