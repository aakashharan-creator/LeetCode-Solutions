class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        hash_edges = dict()
        restricted = set(restricted)
        
        for e in edges:
            if e[0] in hash_edges:
                hash_edges[e[0]].append(e[1])
            else:
                hash_edges[e[0]] = [e[1]]
                
            if e[1] in hash_edges:
                hash_edges[e[1]].append(e[0])
            else:
                hash_edges[e[1]] = [e[0]]
        
        self.visited = set()
        self.dfs(0, hash_edges, restricted)
        
        return len(self.visited)
    
    def dfs(self, curr_node, hash_edges, restricted):
        if curr_node in restricted or curr_node in self.visited:
            return
        
        self.visited.add(curr_node)
        for neighbour in hash_edges[curr_node]:
            self.dfs(neighbour, hash_edges, restricted)