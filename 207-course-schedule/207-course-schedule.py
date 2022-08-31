class Solution:
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edges = dict([(i, set()) for i in range(numCourses)])
        
        for a, b in prerequisites:
            edges[a].add(b)
        
        visited = [False] * numCourses
        rec = [False] * numCourses
        
        for i in range(numCourses):
            if self.dfs(edges, i, visited, rec):
                return False
        return True
        
    def dfs(self, edges, curr_edge, visited, rec):
        visited[curr_edge] = True
        rec[curr_edge] = True
        
        for neighbour in edges[curr_edge]:
            if not visited[neighbour]:
                if self.dfs(edges, neighbour, visited, rec):
                    return True
            elif rec[neighbour]:
                return True
        
        rec[curr_edge] = False
        return False