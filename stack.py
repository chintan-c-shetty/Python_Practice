from collections import deque
from queue import LifoQueue
#implementation using deque time complexity O(1)
#creating deque
stack=deque()
#appending at the front-appendleft()
stack.appendleft(1)
stack.append(2)
stack.appendleft(0)
print(stack.pop())
print(stack)
stack2=LifoQueue()
stack2.put(1)
stack2.put(2)
stack2.put(3)
stack2.put(4)
print(stack2.get())
print(stack2)
 