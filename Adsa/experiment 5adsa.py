class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []  # for Kruskal (edge list)
        self.adj_matrix = [[0] * vertices for _ in range(vertices)]  # for Prim

    # Add edge for Kruskal and Prim
    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])
        self.adj_matrix[u][v] = w
        self.adj_matrix[v][u] = w

    # Utility for Kruskal
    def find(self, parent, i):
        if parent[i] != i:
            parent[i] = self.find(parent, parent[i])
        return parent[i]

    def union(self, parent, rank, x, y):
        if rank[x] < rank[y]:
            parent[x] = y
        elif rank[x] > rank[y]:
            parent[y] = x
        else:
            parent[y] = x
            rank[x] += 1

    # Kruskal's algorithm
    def kruskal(self):
        result = []
        i = e = 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = list(range(self.V))
        rank = [0] * self.V

        while e < self.V - 1 and i < len(self.graph):
            u, v, w = self.graph[i]
            i += 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e += 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)

        print("\nEdges in MST (Kruskal):")
        for u, v, w in result:
            print(f"{u} -- {v} == {w}")

    # Prim's algorithm
    def prim(self):
        key = [float("inf")] * self.V
        parent = [-1] * self.V
        key[0] = 0
        mst_set = [False] * self.V

        for _ in range(self.V):
            min_key = float("inf")
            min_index = -1
            for v in range(self.V):
                if not mst_set[v] and key[v] < min_key:
                    min_key = key[v]
                    min_index = v
            u = min_index
            mst_set[u] = True

            for v in range(self.V):
                if self.adj_matrix[u][v] and not mst_set[v] and key[v] > self.adj_matrix[u][v]:
                    key[v] = self.adj_matrix[u][v]
                    parent[v] = u

        print("\nEdges in MST (Prim):")
        for i in range(1, self.V):
            print(f"{parent[i]} -- {i} == {self.adj_matrix[i][parent[i]]}")


# Menu-driven program
def main():
    vertices = int(input("Enter number of vertices: "))
    g = Graph(vertices)
    edges = int(input("Enter number of edges: "))
    print("Enter edges (u v w):")
    for _ in range(edges):
        u, v, w = map(int, input().split())
        g.add_edge(u, v, w)

    while True:
        print("\n=== MENU ===")
        print("1. Prim's Algorithm")
        print("2. Kruskal's Algorithm")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            g.prim()
        elif choice == "2":
            g.kruskal()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
