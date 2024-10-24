def knapsack(W, wt, val, n):
    """
    Solves the 0/1 knapsack problem using dynamic programming.

    Parameters:
    W: Maximum weight capacity of the knapsack
    wt: List of weights of the items
    val: List of values of the items
    n: Number of items

    Returns:
    Maximum value that can be obtained
    """

    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif wt[i - 1] <= w:
                dp[i][w] = max(val[i - 1] + dp[i - 1][w - wt[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][W]

if __name__ == "__main__":
    val = [60, 100, 120]
    wt = [10, 20, 30]
    W = 50
    n = len(val)
    print(knapsack(W, wt, val, n))
