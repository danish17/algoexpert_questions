# O(n*k) where n = num of children and k = max num of each coin
def maxSpend(coin_vals, num_coins, num_child, max_each):
    childIdx = 0
    coinIdx = 0
    coin_vals = sorted(coin_vals, reverse=True)
    spent = 0
    while childIdx < num_child:
        coins_used = 0
        while coins_used < max_each and childIdx < num_child:
            spent += coin_vals[coinIdx]
            coins_used += 1
            childIdx += 1
        coinIdx += 1
    return spent

maxSpend([1, 2, 3, 4, 7], 5, 3, 2)

