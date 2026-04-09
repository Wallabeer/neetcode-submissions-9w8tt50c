class TimeMap:

    def __init__(self):
        self.Map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.Map[key].append([timestamp, value])
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.Map.keys():
            return ''
        
        target = self.Map[key]
        left = 0
        right = len(target) - 1
        result = ''
        while left <= right:
            mid = (left+ right) // 2
            print(left, right, mid)
            if target[mid][0] <= timestamp:
                result = target[mid][1]
                left = mid + 1
            else:
                right = mid - 1
        return result
                
