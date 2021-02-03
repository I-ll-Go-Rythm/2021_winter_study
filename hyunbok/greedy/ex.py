from queue import PriorityQueue

que = PriorityQueue()

que = PriorityQueue(maxsize=8)

que.put(4)
que.put(3)
que.put(7)

print(que.get())
