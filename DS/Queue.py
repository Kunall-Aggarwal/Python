# LIST 1
q = []

q.append(1)
q.append(2)
q.append(3)
q.append(4)
q.append(5)

q.pop(0)        # pops the first element

not q       # check empty


# LIST 2
q = []

q.insert(0,1)
q.insert(0,2)
q.insert(0,3)
q.insert(0,4)

q.pop()

not queue       # check empty

# MODULE 1
import collections

q = collections.deque()

q.appendleft(1)
q.appendleft(2)
q.appendleft(3)
q.appendleft(4)

q.pop()

#   OR

q.append(1)
q.append(2)
q.append(3)
q.append(4)

q.popleft()

not q       # check Empty


# Module 2
import queue
q = queue.Queue()

q.put(1)
q.put(2)
q.put(3)
q.put(4)

q.get()

