

class Solution:
    graph = list()

    def BFS(self, s):

        # Mark all the vertices as not visited
        visited = set()

        # Create a queue for BFS
        queue = list()

        # Mark the source node as visited and enqueue it
        queue.append(s)
        visited.add(s)

        while queue:

            # Dequeue a vertex and print it
            s = queue[0]
            queue.pop(0)
            print(s, end=" ")

            # Get all adjacent vertices of the dequeued vertex s.
            # If a adjacent has not been visited, then mark it visited and enqueue it
            for node in self.graph[s]:
                if node not in visited:
                    queue.append(node)
                    visited.add(node)


if __name__ == '__main__':
    tester = Solution()
    # ans = tester.func(None)
    # print(ans)
