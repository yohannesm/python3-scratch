#!/usr/bin/python3
from collections import deque

queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.append("Graham")

assert queue.popleft() == 'Eric'
assert queue.pop() == 'Graham'
assert queue.pop() == 'Graham'
