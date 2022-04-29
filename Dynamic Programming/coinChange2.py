def minCoins(coins, target):
    changes = [float("inf")] * (target + 1)
    changes[0] = 0

    for i in range(1, target+1):
        for coin in coins:
            if (i-coin >= 0 or changes[i-coin] != float("inf")):
                changes[i] = min(changes[i], changes[i-coin] + 1)

    return -1 if changes[target] == float("inf") else changes[target]

def main():
    coins = [1,5,7,10]
    target = 19

    print("Min coins required: ", minCoins(coins, target))



if __name__ == "__main__":
    main()
