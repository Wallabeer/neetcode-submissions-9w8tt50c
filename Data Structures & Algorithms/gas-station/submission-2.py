class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        n = len(gas)
        total = 0
        result = 0
        for i in range(n):
            if total < 0:
                print(i)
                result = i
                total = 0
            total += gas[i]
            total -= cost[i]
        return result
            