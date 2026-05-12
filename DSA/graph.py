from collections import deque 
class Solution:
    def dfs(self, graph, start =1 , visited = set()):
        if len(visited) == len(graph.keys()):
            return []
        neighbours = graph[start]
        visited.add(start)
        answer=[start]
        for nei in neighbours:
            if nei not in visited:
                answer += dfs(graph, nei, visited)
        return answer
    def bfs(self, graph, start = 1, visited = set()):
        q = deque()
        q.append(start)
        answer = []
        while len(q) > 0:
            n = len(q)
            for i in range(n):
                ele = q.popleft()
                answer.append(ele)
                visited.add(ele)
                neighbours = graph[ele]
                for nei in neighbours:
                    if nei not in visited:
                        q.append(nei)
        return answer
    
    def num_of_islands(self, grid, i, j):
        if i < 0 or j < 0  or i >= len(grid) or j >= len(grid[0]):
            return 0
        if grid[i][j] == '0' or grid[i][j] == '-1':
            return 0
        

        grid[i][j] = '-1'
        self.num_of_islands(grid, i+1, j)
        self.num_of_islands(grid, i-1, j)
        self.num_of_islands(grid, i, j+1)
        self.num_of_islands(grid, i, j-1)
        
        return 
    
    def numIslands(self, grid):
        count = 0 
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.num_of_islands(grid, i , j)
                    count +=1
        
        return count
        
