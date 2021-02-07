import sys
N = int(sys.stdin.readline())
g = []
for _ in range(N):
    g.append(int(sys.stdin.readline()))

result = 0
cursor = 0
a = 0
stack = [(0, graph[0])]
for i in range(1, n+1):
    cursor = i
    while stack and stack[-1][1]>graph[i]:
        cursor, temp = stack.pop()
        result = max(result, temp*(i-cursor))
    stack.append((cursor, graph[i]))

print(result)
