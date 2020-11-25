
class Solution:
    # Create a set to store visited vertices
    visited = set()
    graph = list()

    # recursive solution
    def DFS(self, node):

        visited = self.visited

        # Mark the current node as visited
        visited.add(node)

        # Recurse for all the nodes adjacent
        for neighbour in self.graph[node]:
            if neighbour not in visited:
                self.DFS(neighbour)

    # stack based iterative solution
    def DFSit(self, s):
        # Initially mark all verices as not visited
        visited = set()

        # Create a stack for DFS
        stack = list()

        # Push the current source node.
        stack.append(s)

        while len(stack):
            # Pop a vertex from stack and print it
            s = stack[-1]
            stack.pop()

            # Stack may contain same vertex twice. So we check visited
            if s not in visited:
                print(s, end=' ')
                visited.add(s)

            # Get all adjacent vertices of the popped vertex s
            # If a adjacent has not been visited, then push it to the stack.
            for node in self.graph[s]:
                if node not in visited:
                    stack.append(node)


if __name__ == '__main__':
    tester = Solution()
    # ans = tester.func(None)
    # print(ans)
