# there is no pre-defined DS such as STACK, int Python
# So we can implement it using LIST and MODULES


# List
stack = []

stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)

stack.pop()

if len(stack):
    print('Not empty')
else:
    print('Empty')


# Modules
import collections

st = collections.deque()

st.append(1)
st.append(2)
st.append(3)
st.append(4)

st.pop()

not st


# Module
import queue
st1 = queue.LifoQueue()

st.put(1)
st.put(2)
st.put(3)
st.put(4)

st.get()        # pop()

