def minCost(stones):
    dp = [0] * len(stones)
    dp[0] = 0
    dp[1] = abs(stones[1] - stones[0])

    for i in range(2, len(stones)):
        jump_1 = abs(stones[i] - stones[i-1]) + dp[i-1]
        jump_2 = abs(stones[i] - stones[i-2]) + dp[i-2]

        dp[i] = min(jump_1, jump_2)

    return dp[len(stones) - 1]

def main():
    stones = [30, 10, 60 ,10, 60, 50]
    print("min cost is: ", minCost(stones))

if __name__ == "__main__":
    main()
