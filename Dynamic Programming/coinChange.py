def minCoins(coins, m) -> int:
    dp = [float("inf")] * (m+1)
    dp[0] = 0

    for i in range(1, m+1):
        for coin in coins:
            if i-coin >= 0 and dp[i-coin] != float("inf"):
                dp[i] = min(dp[i], dp[i-coin] + 1)


    return -1 if dp[m] == float("inf") else dp[m]


def main():
    coinsList = [1,3,4,5,10]
    target = 16

    print("min coins required: ", minCoins(coinsList, target))



if __name__ == "__main__":
    main()
