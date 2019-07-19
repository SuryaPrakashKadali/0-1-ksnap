
val = [int(x) for x in input().split()]   
wt = [int(x) for x in input().split()]   

k = int(input())
n = len(val) 

dp = [[0 for x in range(k+1)] for x in range(n+1)] 
for i in range(n+1): 
    for k in range(k+1): 
        if i==0 or k==0: 
            dp[i][k] = 0
        elif wt[i-1] <= k: 
            dp[i][k] = max(val[i-1] + dp[i-1][k-wt[i-1]],  dp[i-1][k]) 
        else: 
            dp[i][k] = dp[i-1][k] 
            
print(dp[n][k])
