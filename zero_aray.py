coins = [1,2,5,10,15]
value = 345235


def coinChange(self,coins,amount):
    self.coins = sorted(coins)
    self.amount = amount
    coins_new = self.coins.reverse()
    for i in range(len(coins)):
        for items in coins_new:
            if value % items[i] >




