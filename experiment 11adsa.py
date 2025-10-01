def lcs_top_down(X: str, Y: str) -> str:
    """
    Top-down approach using memoization (dictionary).
    Returns the LCS string.
    """
    memo = {}

    def solve(i, j):
        if i == len(X) or j == len(Y):
            return ""
        if (i, j) in memo:
            return memo[(i, j)]

        if X[i] == Y[j]:
            memo[(i, j)] = X[i] + solve(i + 1, j + 1)
        else:
            left = solve(i + 1, j)
            right = solve(i, j + 1)
            memo[(i, j)] = left if len(left) >= len(right) else right

        return memo[(i, j)]

    return solve(0, 0)


def lcs_bottom_up(X: str, Y: str) -> str:
    """
    Bottom-up approach using DP table.
    Returns the LCS string.
    """
    m, n = len(X), len(Y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Build length DP table
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if X[i] == Y[j]:
                dp[i][j] = 1 + dp[i + 1][j + 1]
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])

    # Reconstruct LCS
    i, j = 0, 0
    lcs_result = []
    while i < m and j < n:
        if X[i] == Y[j]:
            lcs_result.append(X[i])
            i += 1
            j += 1
        elif dp[i + 1][j] >= dp[i][j + 1]:
            i += 1
        else:
            j += 1

    return "".join(lcs_result)


def lcs_space_optimized(X: str, Y: str) -> int:
    """
    Space-optimized approach (only returns length).
    Uses rolling arrays.
    """
    m, n = len(X), len(Y)
    prev = [0] * (n + 1)

    for i in range(m - 1, -1, -1):
        curr = [0] * (n + 1)
        for j in range(n - 1, -1, -1):
            if X[i] == Y[j]:
                curr[j] = 1 + prev[j + 1]
            else:
                curr[j] = max(prev[j], curr[j + 1])
        prev = curr

    return prev[0]


# --- Main Program with User Input ---
if __name__ == "__main__":
    X = input("Enter first string: ").strip()
    Y = input("Enter second string: ").strip()

    print("\n--- LCS Results ---")
    print("Top-down LCS:", lcs_top_down(X, Y))
    print("Bottom-up LCS:", lcs_bottom_up(X, Y))
    print("Space-optimized LCS length:", lcs_space_optimized(X, Y))
