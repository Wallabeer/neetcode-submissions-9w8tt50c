class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # ngroups = len(hand)/groupSize
        hand.sort()
        freq = {}
        for num in hand:
            freq[num] = freq.get(num, 0) + 1
        
        for num in hand:
            if freq[num]:
                for i in range(num, num+groupSize):
                    if freq.get(i, 0) >0:
                        freq[i] -= 1
                    else:
                        return False
        return True

            