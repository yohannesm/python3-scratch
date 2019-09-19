#!/usr/bin/python3

def checkListEquality(lst1, lst2):
    if (len(lst1) != len(lst2)):
        return False
    for i in range(len(lst1)):
        if(lst1[i] != lst2[i]):
            return False
    return True


stack = [3, 4, 5]
stack.append(6)
stack.append(7)

print(stack)
assert checkListEquality(stack, [3, 4, 5, 6, 7])
assert stack == [3, 4, 5, 6, 7]
assert stack.pop() == 7
assert stack.pop() == 6
