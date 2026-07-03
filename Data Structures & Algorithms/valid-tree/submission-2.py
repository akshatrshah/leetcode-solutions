class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        seen = [False] * n

        adj = {}

        for a,b in edges:
            x = adj.get(a,[])
            x.append(b)
            adj[a] = x
            y = adj.get(b,[])
            y.append(a)
            adj[b] = y
        
        q = deque()
        q.append((0,-1))

        while q:
            node,parent = q.popleft()
            if seen[node]:
                return False
            seen[node] = True
            for nei in adj.get(node,[]):
                if nei == parent:
                    continue
                q.append((nei,node))
        
        return seen == [True] * n


