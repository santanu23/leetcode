class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        graph = collections.defaultdict(list)
        for edge1, edge2 in edges:
            graph[edge1] += [edge2]
            graph[edge2] += [edge1]
        
        if edges:
            visited = set()
            queue = collections.deque([graph.keys()[0]])
            while queue:
                node = queue.popleft()
                if node in visited:
                    return False
                visited.add(node)
                for neighbour in graph[node]:
                    queue.append(neighbour)
                    graph[neighbour].remove(node)
                graph.pop(node)

        return len(edges) == n - 1 and not graph
