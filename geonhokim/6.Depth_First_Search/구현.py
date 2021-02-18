from typing import List

class myGraph:
    def __init__(self):
        self.graph = {}

    def addInfo(self, startV: int, endV: List[int]):
        self.graph[startV] = endV
    
    def addEdge(self, startV: int, endV: int):
        self.graph[startV].append(endV)
    
    def addVertex(self, V: int):
        self.graph[V] = []

    def dfs_recursive(self, startV, visited = []):
        visited.append(startV)
        
        for endV in self.graph[startV]:
            if endV not in visited:
                self.dfs_recursive(endV, visited)

        return visited

    def dfs(self, startV):
        s = [startV]
        visited = []
        while s:
            nowV = s.pop()
            if nowV not in visited:
                visited.append(nowV)
                s.extend(self.graph[nowV][::-1])

        return visited

g = myGraph()
g.addInfo( 'A', ['B',  'E',  'I'])
g.addInfo( 'B', ['A',  'C'])
g.addInfo( 'C', ['B',  'D'])
g.addInfo( 'D', ['C'])
g.addInfo( 'E', ['A',  'F',  'H'])
g.addInfo( 'F', ['E',  'G'])
g.addInfo( 'G', ['F'])
g.addInfo( 'H', ['E'])
g.addInfo( 'I', ['A',  'J'])
g.addInfo( 'J', ['I'])

a = g.dfs('A')

print(a)