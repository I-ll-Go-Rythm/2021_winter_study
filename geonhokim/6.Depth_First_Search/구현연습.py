from typing import List


class myGraph:
    def __init__(self):
        self.graph = {}
    
    def addInfo(self, startV: int, endV: List[int]):
        self.graph[startV] = endV
    
    def addEdge(self, startV: int, endV: int):
        self.graph[startV].append(endV)
    
    def addVertex(self, startV: int):
        self.graph[startV] = []

    def dfs_recursive(self, startV: int, visited = []):
        visited.append(startV)

        for w in self.graph[startV]:
            if w not in visited:
                self.dfs_recursive(w, visited)
        
        return visited

g = myGraph()
g.addInfo('A', ['B', 'F', 'H'])
g.addInfo('B', ['A', 'C', 'E'])
g.addInfo('C', ['B', 'D'])
g.addInfo('D', ['C'])
g.addInfo('E', ['B'])
g.addInfo('F', ['A', 'G'])
g.addInfo('G', ['F'])
g.addInfo('H', ['A', 'I', 'J'])
g.addInfo('I', ['A', 'I'])
g.addInfo('J', ['H'])

print(g.dfs_recursive('A'))