class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = [False] * n

        adj = defaultdict(list)

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        q = deque()
        q.append((0,-1))

        while q:
            node,parent = q.popleft()
            visited[node] = True
            for nei in adj[node]:
                if nei == parent:
                    continue
                if visited[nei]:
                    return False
                q.append((nei,node))
            
        return visited == [True] * n
                    