def minCoins(coins, target):
    dp = [float("inf")] * (target+1)
    dp[0] = 0

    for i in range(1, target+1):
        for coin in coins:
            if i-coin >= 0 and dp[i-coin] != float("inf"):
                dp[i] = min(dp[i], dp[i-coin]+1)


    return -1 if dp[target] == float("inf") else dp[target]


def main():
    coins = [1,3,4,7,10]
    target = 16

    print("Min coins required: ", minCoins(coins, target))


if __name__ == "__main__":
    main()
