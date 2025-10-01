def knapsack(weights, values, capacity, n):
    # Create a DP table
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(values[i-1] + dp[i-1][w - weights[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]
    
    # Find the selected items
    selected_items = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            selected_items.append((values[i-1], weights[i-1]))
            w -= weights[i-1]
    
    return dp[n][capacity], selected_items


# Example with 5 items
values = [60, 100, 120, 90, 70]
weights = [10, 20, 30, 25, 15]
capacity = 50
n = len(values)

max_profit, selected_items = knapsack(weights, values, capacity, n)

print("Maximum value in Knapsack =", max_profit)
print("Items included (value, weight):")
for v, w in reversed(selected_items):
    print(f"Value = {v}, Weight = {w}")
