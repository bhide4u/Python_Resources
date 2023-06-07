# Depth First Search Algorithm

# In Python 3.8 and above, you can implement the Depth-First Search (DFS) algorithm using recursion or iteration. Here's an explanation of how DFS works using recursion:

# DFS Algorithm using Recursion:

# 1. Define a graph in the form of an adjacency list or matrix, representing the connections between vertices.

# 2. Create a visited set to keep track of the visited vertices during the traversal.

# 3. Implement the DFS function:


def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)  # Process the current vertex

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


# 4. Call the DFS function, providing the graph and the starting vertex:


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

dfs(graph, 'A')


# In this example, we have a graph represented as an adjacency list. The 'dfs' function takes the graph, a starting vertex, and a visited set as parameters. If the visited set is not provided, it is initialized as an empty set.

# The DFS function begins by marking the current vertex (start) as visited and processes it (in this case, printing it). It then recursively calls itself on all unvisited neighbors of the current vertex.

# The recursion continues until there are no more unvisited neighbors. This depth-first exploration ensures that each branch is explored as deeply as possible before backtracking.

# When calling the 'dfs' function with 'graph' and the starting vertex ''A'', the output will be:

'''
A
B
D
E
F
C
'''

# This output represents the order in which the vertices were visited during the DFS traversal.

# DFS can be used for a variety of applications, such as finding connected components, determining if a path exists between two vertices, and exploring all reachable vertices in a graph.

# Note that the DFS algorithm can also be implemented iteratively using a stack data structure instead of recursion. The basic idea remains the same, but instead of using function calls, you would use a stack to keep track of the vertices to visit.