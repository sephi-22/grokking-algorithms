#This was done using ChatGPT as this code wasn't in the book.
#Need to understand this and retype this later.
def knapsack_dynamic_programming(values, weights, capacity):
    n = len(values)
    dp = [[0] * (int(capacity) + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(int(capacity) + 1):
            if int(weights[i - 1]) <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - int(weights[i - 1])], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    # Backtrack to find the selected items
    selected_items = []
    i, j = n, int(capacity)
    while i > 0 and j > 0:
        if dp[i][j] != dp[i - 1][j]:
            selected_items.append(i - 1)
            j -= int(weights[i - 1])
        i -= 1

    return dp[n][int(capacity)], selected_items[::-1]

# Example usage
values = [3000, 2000, 1500]
weights = [4.0, 3.0, 1.0]
capacity = 4.0

max_value, selected_items = knapsack_dynamic_programming(values, weights, capacity)

print("Maximum value:", max_value)
print("Selected items:", selected_items)