class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = [False] * n
        res = 0
        adj = defaultdict(list)

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        
        def func(i):
            if visited[i]:
                return 

            visited[i] = True

            connections = adj[i]

            for nei in connections:
                func(nei)
            

        for i in range(n):
            if visited[i] == False:
                res += 1
                func(i)
        
        return res