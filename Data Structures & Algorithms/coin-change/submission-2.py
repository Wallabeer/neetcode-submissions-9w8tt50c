class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        result = 0
        coins.sort()
        cache = {}
        cache[0] = 0
        def helper(amount):
            result = []
            if amount == 0:
                return 0
            
            if amount in cache:
                return cache[amount]
            
            for coin in coins:
                if amount >= coin:
                    count = helper(amount-coin)
                    if count != -1:
                        result.append(helper(amount-coin))
            
            if result:
                cache[amount] = 1+min(result) 
            else:
                cache[amount] = -1
            
            return cache[amount]
        
        helper(amount)
        print(cache)
        return cache[amount]


                
