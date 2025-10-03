import itertools

def calculate_total_distance(route, distance_matrix):
    """Calculate the total distance of the given route."""
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += distance_matrix[route[i]][route[i + 1]]
    # Add the distance from last city back to the first
    total_distance += distance_matrix[route[-1]][route[0]]
    return total_distance

def travelling_salesman_problem():
    # Step 1: Input number of cities
    n = int(input("Enter the number of cities: "))

    # Step 2: Input distance matrix (a list of lists)
    distance_matrix = []
    print(f"Enter the distance matrix (a {n}x{n} matrix):")
    for i in range(n):
        row = list(map(int, input(f"Enter distances from city {i+1} to all cities: ").split()))
        distance_matrix.append(row)

    # Step 3: Generate all possible routes (permutations)
    cities = list(range(n))
    all_routes = itertools.permutations(cities)

    # Step 4: Calculate the distance for each route and find the shortest one
    shortest_route = None
    shortest_distance = float('inf')

    for route in all_routes:
        total_distance = calculate_total_distance(route, distance_matrix)
        if total_distance < shortest_distance:
            shortest_distance = total_distance
            shortest_route = route

    # Step 5: Output the results
    print(f"\nThe shortest route is: {', '.join([str(city + 1) for city in shortest_route])}")
    print(f"The shortest distance is: {shortest_distance}")

# Run the TSP function
travelling_salesman_problem()
