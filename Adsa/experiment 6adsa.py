INF = 999999

def print_matrix(matrix, V, step):
    print(f"\nMatrix {step}:")
    for i in range(V):
        for j in range(V):
            if matrix[i][j] == INF:
                print("INF", end="\t")
            else:
                print(matrix[i][j], end="\t")
        print()

def floyd_warshall(V, graph):
    # dist initially same as graph
    dist = [row[:] for row in graph]
    print_matrix(dist, V, 0)  # Initial matrix

    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
        print_matrix(dist, V, k + 1)  # Print after each k
    return dist

def main():
    V = int(input("Enter number of vertices: "))
    E = int(input("Enter number of edges: "))
    
    # Initialize graph with INF
    graph = [[INF] * V for _ in range(V)]
    for i in range(V):
        graph[i][i] = 0
    
    print("\nEnter edges in format: u v w (1-based vertices)")
    for _ in range(E):
        u, v, w = map(int, input().split())
        graph[u - 1][v - 1] = w  # directed graph (use both sides if undirected)
    
    floyd_warshall(V, graph)

if __name__ == "__main__":
    main()
