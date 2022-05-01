def minCost(stones):
    prevCosts = [0] * len(stones)
    prevCosts[0] = 0
    prevCosts[1] = abs(stones[0] - stones[1])

    for i in range(2, len(stones)):
        jump_1 = abs(stones[i] - stones[i-1]) + prevCosts[i-1]
        jump_2 = abs(stones[i] - stones[i-2]) + prevCosts[i-2]

        prevCosts[i] = min(jump_1, jump_2)

    return prevCosts[len(stones)-1]

def main():
    rocks = [30,10,60,10,60,50]

    print("Min cost: ", minCost(rocks))

if __name__ == "__main__":
    main()
