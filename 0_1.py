def knapsack_dp(W, wt, val, n):
    """A Dynamic Programming based solution for 0-1 Knapsack problem
    Returns the maximum value that can"""
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]

    # Build table K[][] in bottom up manner
    for i in range(1,n + 1):
        for w in range(1,W + 1):
            # if i == 0 or w == 0:
            #     K[i][w] = 0
            if wt[i - 1] <= w:
                K[i][w] = max(K[i - 1][w],val[i - 1] + K[i-1][w - wt[i-1]])
            else:
                K[i][w] = K[i - 1][w]
    return K


val = [3,4,6,5]
wt = [2,3,1,4]
W = 8
n = len(val)

k = knapsack_dp(W, wt, val, n)
print("Maximum possible profit =", k[n][W])
print(k)

sol = []
value = k[n][W]
for i in range(n,0,-1):
    if value not in k[i-1] and value in k[i]:
        value = value - val[i-1]
        sol.append(1)
    else:
        sol.append(0) 
print(sol[::-1])


    



